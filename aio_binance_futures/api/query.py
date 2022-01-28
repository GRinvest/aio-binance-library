import asyncio
import hmac
from copy import deepcopy
from hashlib import sha256
from time import sleep, time
from typing import Dict
from urllib.parse import urlencode

import ujson
from aiohttp import ClientSession
from loguru import logger

from .error import BinanceApiException


class Api():

    shift_seconds = 0
    recconect = 0
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

    def __set_shift_seconds(self, seconds):
        Api.shift_seconds = seconds

    def __check_response(self, json_wrapper: Dict):
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
                self.__set_shift_seconds(Api.shift_seconds - 1)
            elif code == -1003:
                start = msg.find(' ', msg.find('until'))
                end = msg.find('.', start)
                timer = int((int(msg[start:end-1]) - int(time() * 100)) / 100)
                logger.log('API', f"Binance banned IP. I'll be waiting {timer} sec.")
                sleep(timer)
            else:
                raise BinanceApiException(code, msg)

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

    async def __recconect(self, args, kwargs, sleeping, err):
        if Api.recconect > 10:
            raise BinanceApiException(
                BinanceApiException.RUNTIME_ERROR, f"(Binance Futures Api) [Connector Error]: Exception {err}")
        else:
            logger.error(err)
            Api.timeout += 2
            Api.recconect += 1
            await asyncio.sleep(sleeping)
            return await self.fetch(*args, **kwargs)

    async def _fetch(self, *args, **kwargs) -> Dict:
        _kwargs_deep = deepcopy(kwargs)
        self.headers = {
            'Content-Type': 'application/json',
            'user-agent': "aiobinance-lib-py",
            "client_SDK_Version": "aiobinance-lib-2.0.1-py3.10"
        }
        if args[0]:
            assert self.key is not None, \
                "For job this function needs api key binance, please add in Client()"
            assert self.secret is not None, \
                "For job this function needs api secret binance, please add in Client()"
            self.headers.update({"X-MBX-APIKEY": self.key})
            self.__crypto_key(kwargs)
        url = self.host + args[3]
        request_data = {
            'method': args[1],
            'url': url,
            'timeout': Api.timeout
        }
        if args[1] == 'GET':
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
                async with self.session.request(**request_data) as responce:
                    _responce = await responce.text()
            else:
                async with ClientSession() as session:
                    async with session.request(**request_data) as responce:
                        _responce = await responce.text()
            Api.weight = responce.headers['X-MBX-USED-WEIGHT-1M']
        except Exception as err:
            return await self.__recconect(args, _kwargs_deep, 3, err)
        else:
            if Api.recconect > 0:
                Api.recconect = 0
                Api.timeout = 2
            logger.log(
                'API',
                "      Function {}() work Ok! Ping: {:.2f} ms. Weight: {}".format(
                    args[2],
                    (time() * 1000)-start_time,
                    Api.weight))
            try:
                res_json = ujson.loads(_responce)
            except ValueError:
                raise BinanceApiException(
                    BinanceApiException.INPUT_ERROR,
                    f"(Binance Futures Api) [ValueError]: {_responce}")
            else:
                self.__check_response(res_json)
                if self.show_limit_usage:
                    res_json['limit_usage'] = Api.weight
                if self.show_header:
                    res_json['header'] = responce.headers
                return res_json
