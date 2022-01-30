import asyncio

from aio_binance.futures.usdt import WsClient


async def callback_event(data: dict):
    """
    Args:
        data (dict): Combined stream events are wrapped as follows: {"stream":"<streamName>","data":<rawPayload>}
    """
    print(data)


async def main():
    """
    WebSocket connections have a limit of 10 incoming messages per second.
    A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
    A single connection can listen to a maximum of 200 streams.
    """
    ws = WsClient()
    stream = [
        ws.stream_liquidation_order(),
        ws.stream_book_ticker(),
        ws.stream_ticker('BTCUSDT')
    ]
    res = await asyncio.gather(*stream)
    await ws.subscription_streams(res, callback_event)

asyncio.run(main())
