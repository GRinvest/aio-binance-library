from sys import stderr

from loguru import logger

from aio_binance.__version__ import __version__
from .api.account import Account
from .api.market import Market
from .api.query import Api
from .api.stream import DataStream
from .websocket.query import Ws
from .websocket.streams import Streams


def _snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


class Client(Api, Market, DataStream, Account):

    logger.level("API", no=10)

    def __init__(
            self,
            key: str = None,
            secret: str = None,
            testnet: bool = False,
            debug: str = "debug",
            **kwargs):
        logger.remove()
        logger.add(stderr, colorize=True,
                   format="<green>{level}</green>:     <cyan>{message}</cyan>",
                   level=debug.upper(),
                   enqueue=True)
        super().__init__(key=key, secret=secret, testnet=testnet, version=__version__, **kwargs)

    # UTILS

    def _to_api(self, data: dict | list) -> dict | list:
        _data = None
        if isinstance(data, dict):
            _data = dict()
            for key, value in data.items():
                _data[_snake_to_camel(key)] = value
        elif isinstance(data, list):
            _data = list()
            for item in data:
                _d = dict()
                for key, value in item.items():
                    _d[_snake_to_camel(key)] = value
                _data.append(_d)
        return _data


class WsClient(Ws, Streams):
    logger.level("ACCOUNT", no=10)
    logger.level("WEBSOCKET", no=10)

    def __init__(
            self,
            listen_key: str = None,
            debug='debug',
            **kwargs):
        logger.remove()
        logger.add(stderr, colorize=True,
                   format="<green>{level}</green>:     <cyan>{message}</cyan>",
                   level=debug.upper(),
                   enqueue=True)
        super().__init__(listen_key=listen_key, **kwargs)


