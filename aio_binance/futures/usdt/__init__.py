from sys import stderr

from loguru import logger

from aio_binance.futures.usdt.api.methods.account import Account
from aio_binance.futures.usdt.api.methods.market import Market
from aio_binance.futures.usdt.api.methods.stream import DataStream
from .api.query import Api
from .websocket.query import Ws
from .websocket.streams import Streams

logger.level("API", no=10)
logger.level("ACCOUNT", no=10)
logger.level("WEBSOCKET", no=10)
logger.level("TIMER", no=10)


class Client(Api, Market, DataStream, Account):

    def __init__(self,
                 key: str = None,
                 secret: str = None,
                 testnet=False,
                 debug: str = "debug",
                 timeout=5,
                 **kwargs):
        """**Client connection Binance Api**

        Args:
            key: Binance Api key
            secret: Binance Api Secret
            testnet: Work testnet True or False
            debug: Debug level 'debug', 'info', 'error', default: 'debug'
            timeout: Timeout in second for reconnect
        Keyword Args:
            session: (optional) aiohttp.ClientSession()
        """
        logger.remove()
        logger.add(stderr, colorize=True,
                   format="<green>{level}</green>:     <cyan>{message}</cyan>",
                   level=debug.upper(),
                   enqueue=True)
        super().__init__(key=key,
                         secret=secret,
                         testnet=testnet,
                         timeout=timeout,
                         **kwargs)

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


class WsClient(Ws, Streams):

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


