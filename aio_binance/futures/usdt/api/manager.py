import sys

from loguru import logger

from aio_binance.futures.usdt.api.methods.account import Account
from aio_binance.futures.usdt.api.methods.market import Market
from aio_binance.futures.usdt.api.methods.stream import DataStream
from aio_binance.futures.usdt.api.query import Api


class FactoryApi(Api,
                 Market,
                 DataStream,
                 Account):

    # UTILS
    @staticmethod
    def _snake_to_camel(snake_str: str) -> str:
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    def _to_api(self, data: dict | list) -> dict | list:
        _data = None
        if isinstance(data, dict):
            _data = dict()
            for key, value in data.items():
                _data[self._snake_to_camel(key)] = value
        elif isinstance(data, list):
            _data = list()
            for item in data:
                _d = dict()
                for key, value in item.items():
                    _d[self._snake_to_camel(key)] = value
                _data.append(_d)
        return _data
