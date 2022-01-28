from sys import stderr

from loguru import logger

from futures.query import Api


class Client(Api):

    logger.level("API", no=10)

    def __init__(
            self,
            key: str = None,
            secret: str = None,
            testnet: bool = False,
            debug: str = "debug"):
        logger.remove()
        logger.add(stderr, colorize=True,
                   format="<green>{level}</green>:     <cyan>{message}</cyan>",
                   level=debug.upper(),
                   enqueue=True)
        super().__init__(key=key, secret=secret, testnet=testnet)

    # MARKETS
    # ACCOUNT(including orders and trades)
    from futures.account import (account, adl_quantile, api_trading_status,
                                 balance, cancel_batch_order,
                                 cancel_open_orders, cancel_order,
                                 change_leverage, change_margin_type,
                                 change_multi_asset_mode, change_position_mode,
                                 commission_rate, countdown_cancel_order,
                                 force_orders, get_account_trades,
                                 get_all_orders, get_income_history,
                                 get_multi_asset_mode, get_open_orders,
                                 get_orders, get_position_margin_history,
                                 get_position_mode, get_position_risk,
                                 leverage_brackets,
                                 modify_isolated_position_margin,
                                 new_batch_order, new_order, new_order_test,
                                 query_order)
    from futures.market import (agg_trades, asset_Index, blvt_kline,
                                book_ticker, continuous_klines, depth,
                                exchange_info, funding_rate, historical_trades,
                                index_info, index_price_klines, klines,
                                mark_price, mark_price_klines, open_interest,
                                ping, ticker_24hr_price_change, ticker_price,
                                time, trades)
    # STREAMS
    from futures.stream import (close_listen_key, new_listen_key,
                                update_listen_key)
