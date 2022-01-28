from sys import stderr

from loguru import logger

from aio_binance.__version__ import __version__
from .api.query import Api
from .websocket.query import Ws

logger.remove()
logger.add(stderr, colorize=True,
           format="<green>{level}</green>:     <cyan>{message}</cyan>",
           enqueue=True)


class Client(Api):

    logger.level("API", no=10)

    def __init__(
            self,
            key: str = None,
            secret: str = None,
            testnet: bool = False,
            debug: str = "error"):
        logger.level(debug.upper())
        super().__init__(key=key, secret=secret, testnet=testnet, version=__version__)

    # ACCOUNT(including orders and trades)
    from .api.account import (account, adl_quantile, api_trading_status,
                              balance, cancel_batch_order, cancel_open_orders,
                              cancel_order, change_leverage,
                              change_margin_type, change_multi_asset_mode,
                              change_position_mode, commission_rate,
                              countdown_cancel_order, force_orders,
                              get_account_trades, get_all_orders,
                              get_income_history, get_multi_asset_mode,
                              get_open_orders, get_orders,
                              get_position_margin_history, get_position_mode,
                              get_position_risk, leverage_brackets,
                              modify_isolated_position_margin, new_batch_order,
                              new_order, new_order_test, query_order)
    # MARKETS
    from .api.market import (agg_trades, asset_Index, blvt_kline, book_ticker,
                             continuous_klines, depth, exchange_info,
                             funding_rate, historical_trades, index_info,
                             index_price_klines, klines, mark_price,
                             mark_price_klines, open_interest, ping,
                             ticker_24hr_price_change, ticker_price, time,
                             trades)
    # STREAMS
    from .api.stream import close_listen_key, new_listen_key, update_listen_key


class WsClient(Ws):
    logger.level("ACCOUNT", no=10)
    logger.level("WEBSOCKET", no=10)

    def __init__(
            self,
            listen_key: str = None,
            debug='error',
            **kwargs):
        logger.level(debug.upper())
        super().__init__(listen_key=listen_key, **kwargs)

    from .websocket.streams import (agg_trade, blvt_info, blvt_kline,
                                    book_ticker, composite_index,
                                    continuous_kline, diff_book_depth, kline,
                                    liquidation_order, mark_price, mini_ticker,
                                    partial_book_depth, subscription_streams,
                                    ticker, user_data)
