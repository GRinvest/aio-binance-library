import asyncio

from aio_binance_futures import WsClient

SYMBOL = 'BTCUSDT'


async def event_mark_price(data: dict):
    print(data)


async def event_liquidation_order(data: dict):
    print(data)


async def event_kline(data: dict):
    print(data)


async def event_depth_update(data: dict):
    print(data)


async def adapter_event(data: dict):
    event = data.get('e')
    if event == 'markPriceUpdate':
        await event_mark_price(data)
    elif event == 'forceOrder':
        await event_liquidation_order(data)
    elif event == 'kline':
        await event_kline(data)
    elif event == 'depthUpdate':
        await event_depth_update(data)
    else:
        print(data)


async def main():
    tasks = [
        asyncio.create_task(
            WsClient().mark_price(
                SYMBOL,
                callback_event=adapter_event)),
        asyncio.create_task(
            WsClient().liquidation_order(
                SYMBOL,
                callback_event=adapter_event)),
        asyncio.create_task(
            WsClient().kline(
                SYMBOL,
                '1m',
                callback_event=adapter_event)),
        asyncio.create_task(
            WsClient().partial_book_depth(
                SYMBOL,
                callback_event=adapter_event))
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
