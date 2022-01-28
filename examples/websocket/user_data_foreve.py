import asyncio

from aio_binance_futures.websocket.account import UserSession

KEY = 'Api_Key_Binance'
SECRET = 'Api_Secret_Binance'


async def calback_event(data: dict):
    print(data)


async def main():
    while True:
        async with UserSession(KEY, SECRET, calback_event):
            pass

asyncio.run(main())
