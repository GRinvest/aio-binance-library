import asyncio

from aio_binance.futures.usdt import Client, WsClient
from loguru import logger

KEY = 'Api_Key_Binance'
SECRET = 'Api_Secret_Binance'


async def calback_event(data: dict):
    print(data)


async def update_key(api: Client, sleep: int = 60*55):
    """
    A User Data Stream is valid for 60 minutes after api.new_listen_key()
    Doing a on a will extend its validity for 60 minutes.

    Args:
        api (Client): instance Api client
        sleep (int, optional): [description]. Defaults to 55 min.
    """
    first = True
    while True:
        if first:
            first = False
            await asyncio.sleep(sleep)
        try:
            await api.update_listen_key()
        except Exception as e:
            logger.error(e)
            await asyncio.sleep(60)
            continue
        else:
            logger.debug(f'Success update listen Key. Try {sleep} min...')
            await asyncio.sleep(sleep)


async def steam_account():
    """https://binance-docs.github.io/apidocs/futures/en/#user-data-streams
    """
    api = Client(KEY, SECRET, debug=True)
    while True:
        try:
            res = await api.new_listen_key()
        except Exception as e:
            logger.error(e)
            await asyncio.sleep(60)
            continue
        else:
            await asyncio.wait(
                [
                    WsClient(res['listenKey']).user_data(calback_event),
                    update_key(api)
                ],
                return_when=asyncio.FIRST_COMPLETED
            )
        finally:
            try:
                await api.close_listen_key()
            except Exception as e:
                logger.error(e)
                await asyncio.sleep(60)

asyncio.run(steam_account())
