from sys import stderr

from loguru import logger

from websocket.query import Ws


class WsClient(Ws):
    logger.level("ACCOUNT", no=10)
    logger.level("WEBSOCKET", no=10)

    def __init__(
            self,
            listen_key: str = None,
            **kwargs):
        logger.remove()
        logger.add(stderr, colorize=True,
                   format="<green>{level}</green>:     <cyan>{message}</cyan>",
                   level=kwargs.get('debug', 'debug').upper(),
                   enqueue=True)
        super().__init__(listen_key=listen_key, **kwargs)

    from websocket.streams import (agg_trade, blvt_info, blvt_kline,
                                   book_ticker, composite_index,
                                   continuous_kline, diff_book_depth, kline,
                                   liquidation_order, mark_price, mini_ticker,
                                   partial_book_depth, subscription_streams,
                                   ticker, user_data)
