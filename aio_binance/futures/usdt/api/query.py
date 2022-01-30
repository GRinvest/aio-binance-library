import hmac
from copy import deepcopy
from hashlib import sha256
from time import sleep, time
from typing import Dict
from urllib.parse import urlencode

import ujson
from aiohttp import ClientSession
from loguru import logger

from aio_binance.error_handler.error import BinanceException


def _set_shift_seconds(seconds) -> None:
    Api.shift_seconds = seconds


class Api:

    shift_seconds = 0
    reconnect = 0
    weight = 0
    timeout = 5

    def __init__(self, **kwargs):
        self.key = kwargs.get('key')
        self.secret = kwargs.get('secret')
        self.show_limit_usage = kwargs.get('show_limit_usage')
        self.show_header = kwargs.get('show_header')
        self.host = 'https://testnet.binancefuture.com' \
            if kwargs.get('testnet') \
            else 'https://fapi.binance.com'
        self.session: ClientSession = None
        self.headers = {}
        self.agent = kwargs.get('agent', 'aio-binance-library')
        self.version = kwargs.get('version')

    async def _check_response(self, json_wrapper: dict | list) -> None | dict:
        code = 200
        msg = ""
        if isinstance(json_wrapper, list):
            for item in json_wrapper:
                if isinstance(item, Dict) and \
                        item.get('code') and \
                        item['code'] != 200:
                    code = item['code']
                    msg = json_wrapper
                    break
        else:
            if json_wrapper.get("code"):
                code = int(json_wrapper["code"])
                msg = json_wrapper.get("msg", "")
        if code != 200:
            if code == -1021:
                _set_shift_seconds(Api.shift_seconds - 1)
            elif code == -1003:
                start = msg.find(' ', msg.find('until'))
                end = msg.find('.', start)
                timer = int((int(msg[start:end - 1]) - int(time() * 100)) / 100)
                logger.log('API', f"Binance banned IP. I'll be waiting {timer} sec.")
                sleep(timer)
            raise BinanceException(code, msg)

    def __crypto_key(self, params: Dict) -> None:
        params.update({
            'recvWindow': 60000,
            'timestamp': int((time() + Api.shift_seconds - 1) * 1000)
        })
        params_str = urlencode(params).encode('utf-8')
        sign = hmac.new(
            key=bytearray(self.secret, encoding='utf-8'),
            msg=params_str,
            digestmod=sha256
        ).hexdigest()
        params.update({'signature': str(sign)})

    async def __reconnect(self, sleeping, err):
        if Api.reconnect > 10:
            raise BinanceException(
                500,
                f"(Binance Futures Api) Sorry )-: My attempts to connect have dried up." +
                f"More than 10. I exit | Exception {err}")
        else:
            Api.timeout += 2
            Api.reconnect += 1
            sleeping += Api.reconnect
            logger.warning(f"(Binance Futures Api) Unable to connect {self.host}," +
                           f" I'll wait {sleeping} sec. and try again," +
                           f" effort № {Api.reconnect} | Such a mistake: {err}")
            sleep(sleeping)
            return await self._fetch(*self._args, **self._kwargs_deep)

    async def _fetch(self, *args, **kwargs) -> Dict:
        result = {}
        self._args = args
        self._kwargs_deep = deepcopy(kwargs)
        self.headers = {
            'Content-Type': 'application/json',
            'user-agent': self.agent,
            "client_SDK_Version": f"aio-binance-library v{self.version}-py3.10"
        }
        if 'private' in args[1]:
            assert self.key is not None, \
                f"For job function {args[1]}() needs api key binance, please add in Client()"
            assert self.secret is not None, \
                f"For job function {args[1]}() needs api secret binance, please add in Client()"
            self.headers.update({"X-MBX-APIKEY": self.key})
            self.__crypto_key(kwargs)
        url = self.host + args[2]
        request_data = {
            'method': args[0],
            'url': url,
            'timeout': Api.timeout
        }
        if args[0] == 'GET':
            request_data['headers'] = self.headers
            request_data['params'] = kwargs if kwargs.keys() else None
        else:
            self.headers.update({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
            request_data['headers'] = self.headers
            request_data['data'] = kwargs if kwargs.keys() else None
        try:
            start_time = time() * 1000
            if self.session:
                async with self.session.request(**request_data) as response:
                    _response = await response.text()
            else:
                async with ClientSession() as session:
                    async with session.request(**request_data) as response:
                        _response = await response.text()
            Api.weight = response.headers['X-MBX-USED-WEIGHT-1M']\
                if int(response.headers['X-MBX-USED-WEIGHT-1M']) > 0\
                else response.headers['X-MBX-ORDER-COUNT-1M']
        except Exception as err:
            return await self.__reconnect(5, err)
        else:
            if Api.reconnect > 0:
                Api.reconnect = 0
                Api.timeout = 2
            logger.log(
                'API',
                "      Request {}() Worked well! Ping: {:.2f} ms. Limit usage: {}".format(
                    args[1],
                    (time() * 1000)-start_time,
                    Api.weight))
            try:
                res_json = ujson.loads(_response)
            except ValueError:
                raise BinanceException(
                    -1,
                    f"(Binance Futures Api) [Json Value Error] response: {_response}")
            else:
                await self._check_response(res_json)
                result['data'] = res_json
                if self.show_limit_usage:
                    result['limit_usage'] = Api.weight
                if self.show_header:
                    result['header'] = response.headers
                return result
