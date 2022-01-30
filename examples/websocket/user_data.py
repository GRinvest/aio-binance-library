import asyncio

from loguru import logger

from aio_binance.futures.usdt import Client, WsClient

KEY = 'Api_Key_Binance'
SECRET = 'Api_Secret_Binance'


async def callback_event(data: dict):
    print(data)


async def steam_account():
    """https://binance-docs.github.io/apidocs/futures/en/#user-data-streams
    """
    api = Client(KEY, SECRET)
    res = await api.create_private_listen_key()
    await WsClient(res['listenKey']).stream_user_data(callback_event)

try:
    asyncio.run(steam_account())
except KeyboardInterrupt:
    logger.info('Close Program Ctrl C')
