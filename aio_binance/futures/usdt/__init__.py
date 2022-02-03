from sys import stderr
import asyncio
import aiohttp
from loguru import logger
import aio_binance.futures.usdt.api.manager
from .api import manager

from .websocket.query import Ws
from .websocket.streams import Streams

logger.level("API", no=10)
logger.level("ACCOUNT", no=10)
logger.level("WEBSOCKET", no=10)
logger.level("TIMER", no=10)


class Client(manager.FactoryApi):

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


class ApiSession(manager.FactoryApi):

    def __init__(self,
                 key: str = None,
                 secret: str = None,
                 testnet=False,
                 debug: str = "debug",
                 timeout=5,
                 **kwargs):
        """**Binance Api Session**

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

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()
        self.session = None
        await asyncio.sleep(0.1)


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

