import asyncio

from aio_binance.futures.usdt import Client, WsClient
from loguru import logger


class UserSession:

    def __init__(self, key: str, secret: str, calback_event):
        self.calback_event = calback_event
        self._api = Client(key, secret)

    async def __aenter__(self):
        res = await self._api.new_listen_key()
        logger.log("ACCOUNT", '  listenKey add success  Connected')
        await asyncio.wait(
            [
                WsClient(res['listenKey']).user_data(self.calback_event),
                self.__update_key()
            ],
            return_when=asyncio.FIRST_COMPLETED
        )
        raise asyncio.CancelledError

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is not None:
            logger.error(exc)
        logger.log("ACCOUNT", '  Close User Session')
        await self._api.close_listen_key()

    async def __update_key(self):
        """
        A User Data Stream is valid for 60 minutes after api.new_listen_key()
        Doing a on a will extend its validity for 60 minutes.

        Args:
            api (Client): instance Api client
            sleep (int, optional): [description]. Defaults to 55 min.
        """
        sleep = 60*55
        first = True
        while True:
            if first:
                first = False
                await asyncio.sleep(sleep)
            await self._api.update_listen_key()
            logger.log("ACCOUNT", f'  Success update listen Key. Try 55 min...')
            await asyncio.sleep(sleep)
