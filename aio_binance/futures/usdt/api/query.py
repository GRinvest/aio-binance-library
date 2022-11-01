import hmac
import time
from copy import deepcopy
from hashlib import sha256
from typing import Dict
from urllib.parse import urlencode

import ujson
from aiohttp import ClientSession
from loguru import logger

from aio_binance.__version__ import __version__
from aio_binance.error_handler.error import BinanceException
from aio_binance.timer import AioTimer


class Api:

    SHIFT_SECONDS = 0
    RECONNECT = 0
    WEIGHT = 0

    def __init__(self, **kwargs):
        self.key = kwargs.get('key')
        self.secret = kwargs.get('secret')
        self.show_limit_usage = kwargs.get('show_limit_usage')
        self.show_header = kwargs.get('show_header')
        self.host = 'https://testnet.binancefuture.com' \
            if kwargs.get('testnet') \
            else 'https://fapi.binance.com'
        self.session: ClientSession = None
        self.timeout = kwargs.get('timeout', 5)
        self.__init_params(self.timeout)
        self.agent = kwargs.get('agent', 'aio-binance-library')

    @classmethod
    def __init_params(cls, timeout):
        cls.HEADERS = {
            "client_SDK_Version": f"aio-binance-library v{__version__}-py3.10"
        }
        cls.TIMEOUT = timeout

    @classmethod
    def __set_shift_seconds(cls, seconds) -> None:
        cls.SHIFT_SECONDS = seconds

    @classmethod
    async def __check_response(cls, json_wrapper: dict | list) -> None:
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
                cls.__set_shift_seconds(cls.SHIFT_SECONDS - 1)
            elif code == -1003:
                start = msg.find(' ', msg.find('until'))
                end = msg.find('.', start)
                timer = int((int(msg[start:end - 1]) - int(time.time() * 100)) / 100)
                logger.log('API', f"Binance banned IP. I'll be waiting {timer} sec.")
                time.sleep(timer)
            raise BinanceException(code, msg)

    def __crypto_key(self, params: Dict) -> None:
        params.update({
            'recvWindow': 60000,
            'timestamp': int((time.time() + self.SHIFT_SECONDS - 1) * 1000)
        })
        params_str = urlencode(params).encode('utf-8')
        sign = hmac.new(
            key=bytearray(self.secret, encoding='utf-8'),
            msg=params_str,
            digestmod=sha256
        ).hexdigest()
        params.update({'signature': str(sign)})

    async def __reconnect(self, sleeping, err):
        if self.RECONNECT > 10:
            raise BinanceException(
                500,
                f"(Binance Futures Api) Sorry )-: My attempts to connect have dried up." +
                f"More than 10. I exit | Exception {err}")
        else:
            self.TIMEOUT += 2
            self.RECONNECT += 1
            sleeping += self.RECONNECT
            logger.warning(f"(Binance Futures Api) Unable to connect {self.host}," +
                           f" I'll wait {sleeping} sec. and try again," +
                           f" effort № {self.RECONNECT}")
            time.sleep(sleeping)
            return await self._fetch(*self._args, **self._kwargs_deep)

    async def _fetch(self, *args, **kwargs) -> Dict:
        result = {}
        self._args = args
        self._kwargs_deep = deepcopy(kwargs)
        self.HEADERS.update({'user-agent': self.agent})
        if 'private' in args[1]:
            assert self.key is not None, \
                f"For job function {args[1]}() needs api key binance, please add in Client()"
            assert self.secret is not None, \
                f"For job function {args[1]}() needs api secret binance, please add in Client()"
            self.HEADERS.update({"X-MBX-APIKEY": self.key})
            self.__crypto_key(kwargs)
        else:
            self.HEADERS.pop("X-MBX-APIKEY", None)
        url = self.host + args[2]
        request_data = {
            'method': args[0],
            'url': url,
            'timeout': self.TIMEOUT
        }
        if args[0] == 'GET':
            self.HEADERS.update({'Content-Type': 'application/json'})
            request_data['params'] = kwargs if kwargs.keys() else None
        else:
            self.HEADERS.update({'Content-Type': 'application/x-www-form-urlencoded'})
            request_data['data'] = kwargs if kwargs.keys() else None
        request_data['headers'] = self.HEADERS
        try:
            async with AioTimer(name=f'Binance Futures Api request {args[2]}'):
                if self.session:
                    async with self.session.request(**request_data) as response:
                        _response = await response.text()
                else:
                    async with ClientSession() as session:
                        async with session.request(**request_data) as response:
                            _response = await response.text()
            self.WEIGHT = response.headers['X-MBX-USED-WEIGHT-1M']\
                if int(response.headers['X-MBX-USED-WEIGHT-1M']) > 0\
                else response.headers['X-MBX-ORDER-COUNT-1M']
        except Exception as err:
            if 'private' in args[1]:
                raise BinanceException(-8888, err)
            else:
                return await self.__reconnect(5, err)
        else:
            if self.RECONNECT > 0:
                self.RECONNECT = 0
                self.TIMEOUT = self.timeout
            logger.log(
                'API',
                "      Request {}() Worked well!. Limit usage: {}".format(
                    args[1],
                    self.WEIGHT))
            try:
                res_json = ujson.loads(_response)
            except ValueError:
                raise BinanceException(
                    -1,
                    f"(Binance Futures Api) [Json Value Error] response: {_response}")
            else:
                await self.__check_response(res_json)
                result['data'] = res_json
                if self.show_limit_usage:
                    result['limit_usage'] = self.WEIGHT
                if self.show_header:
                    result['header'] = response.headers
                return result['data']
