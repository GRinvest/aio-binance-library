import asyncio

from loguru import logger

from aio_binance.futures.usdt.websocket.account import UserSession

KEY = 'Key_Binance_Api'
SECRET = 'Secret_Binance_Api'


async def callback_event(data: dict):
    print(data)


async def main():
    while True:
        async with UserSession(KEY, SECRET, debug='debug') as session:
            await session.run(callback_event)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    logger.info('Close Program Ctrl C')

