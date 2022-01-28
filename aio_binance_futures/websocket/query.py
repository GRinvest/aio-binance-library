import asyncio
import socket

import aiohttp
from loguru import logger


class Ws:

    def __init__(self, **kwargs):
        self.listen_key: str = kwargs.get('listen_key')
        self.reply_timeout: int = kwargs.get('reply_timeout', 180)
        self.ping_timeout: int = kwargs.get('ping_timeout', 300)
        self.sleep_time: int = kwargs.get('sleep_time', 3)

    async def _listen_forever(self, path: str, event: object) -> None:
        _url = self.__create_url(path)
        self.quit = False
        while True:
            if self.quit:
                break
            async with aiohttp.ClientSession() as client:
                async with client.ws_connect(_url, autoclose=False, autoping=False, ssl=True) as self.ws:
                    logger.log('WEBSOCKET', f'Creating new connection {_url}')
                    await self.__dispatch(event)

    async def __dispatch(self, event) -> None:
        while True:
            if self.quit:
                break
            try:
                msg = await self.ws.receive(timeout=self.reply_timeout)
            except (asyncio.TimeoutError, TimeoutError):
                try:
                    await self.ws.ping()
                    msg = await self.ws.receive(timeout=self.ping_timeout)
                    if msg.type == aiohttp.WSMsgType.PONG:
                        continue
                except:
                    logger.log(
                        'WEBSOCKET',
                        f'Ping error - retrying connection in {self.sleep_time} sec (Ctrl-C to quit)')
                    await asyncio.sleep(self.sleep_time)
                    if self.listen_key:
                        self.quit = True
                    break
            except socket.gaierror:
                logger.log(
                    'WEBSOCKET',
                    f'Socket error - retrying connection in {self.sleep_time} sec (Ctrl-C to quit)')
                await asyncio.sleep(self.sleep_time)
                continue
            except ConnectionRefusedError:
                logger.log(
                    'WEBSOCKET',
                    'Nobody seems to listen to this endpoint. Please check the URL.')
                logger.log(
                    'WEBSOCKET',
                    f'Retrying connection in {self.sleep_time} sec (Ctrl-C to quit)')
                await asyncio.sleep(self.sleep_time)
                continue
            else:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    await event(msg.json())
                elif msg.type == aiohttp.WSMsgType.PING:
                    await self.ws.pong()
                elif msg.type == aiohttp.WSMsgType.PONG:
                    logger.log(
                    'WEBSOCKET',
                    'Pong received')
                else:
                    if msg.type == aiohttp.WSMsgType.CLOSE:
                        await self.ws.close()
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        logger.error(
                            f"Error during receive {self.ws.exception()}")
                    elif msg.type == aiohttp.WSMsgType.CLOSED:
                        pass
                    break

    def __create_url(self, path):
        if self.listen_key:
            _host = 'wss://fstream-auth.binance.com'
            if path.find('listenKey') >= 0:
                return f"{_host}/ws/{self.listen_key}?{path}={self.listen_key}"
            elif path.find('streams') >= 0:
                return f"{_host}/stream?{path}&listenKey={self.listen_key}"
            else:
                return f"{_host}/ws/{path}?listenKey={self.listen_key}"
        else:
            _host = 'wss://fstream.binance.com'
            if path.find('streams') >= 0:
                return f"{_host}/stream?{path}"
            else:
                return f"{_host}/ws/{path}"
