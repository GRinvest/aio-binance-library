import sys

import ujson


async def change_position_mode(self, dualSidePosition: str, **kwargs):
    """
    |
    | **Change Position Mode (TRADE)**
    | *Change user's position mode (Hedge Mode or One-way Mode) on EVERY symbol*
    :API endpoint: ``POST /fapi/v1/positionSide/dual``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#change-position-mode-trade
    :parameter dualSidePosition: string

    |
    """
    params = {"dualSidePosition": dualSidePosition, **kwargs}
    url_path = "/fapi/v1/positionSide/dual"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, **params)


async def get_position_mode(self, kwargs):
    """
    |
    | **Get Current Position Mode (USER_DATA)**
    | *Get user's position mode (Hedge Mode or One-way Mode) on EVERY symbol*
    :API endpoint: ``GET /fapi/v1/positionSide/dual``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-current-position-mode-user_data

    |
    """
    url_path = "/fapi/v1/positionSide/dual"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, kwargs)


async def change_multi_asset_mode(self, multiAssetsMargin: str, **kwargs):
    """
    |
    | **Change Multi-Assets Mode (TRADE)**
    | *Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol*
    :API endpoint: ``POST /fapi/v1/multiAssetsMargin``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#change-multi-assets-mode-trade
    :parameter multiAssetsMargin: string; "true": Multi-Assets Mode; "false": Single-Asset Mode

    |
    """
    params = {"multiAssetsMargin": multiAssetsMargin, **kwargs}
    url_path = "/fapi/v1/multiAssetsMargin"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, **params)


async def get_multi_asset_mode(self, kwargs):
    """
    |
    | **Get Current Multi-Assets Mode (USER_DATA)**
    | *Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol*
    :API endpoint: ``GET /fapi/v1/multiAssetsMargin``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-current-multi-assets-mode-user_data

    |
    """
    url_path = "/fapi/v1/multiAssetsMargin"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, kwargs)


async def new_order(self, symbol: str, side: str, type: str, **kwargs):
    """
    |
    | **New Order (TRADE)**
    | *Send a new order*
    :API endpoint: ``POST /fapi/v1/order``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#new-order-trade
    :parameter symbol: string
    :parameter side: string
    :parameter type: string
    :parameter positionSide: optional string. async default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be passed in Hedge Mode.
    :parameter timeInForce: optional string
    :parameter quantity: optional float
    :parameter reduceOnly: optional string
    :parameter price: optional float
    :parameter newClientOrderId: optional string. An unique ID among open orders. Automatically generated if not sent.
    :parameter stopPrice: optional float. Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter closePosition: optional string. true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
    :parameter activationPrice: optional float. Use with TRAILING_STOP_MARKET orders, async default is the latest price (supporting different workingType).
    :parameter callbackRate: optional float. Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
    :parameter workingType: optional string. stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". async default "CONTRACT_PRICE".
    :parameter priceProtect: optional string. "TRUE" or "FALSE", async default "FALSE". Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter newOrderRespType: optional float. "ACK" or "RESULT", async default "ACK".

    |
    """
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/fapi/v1/order"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, **params)


async def new_order_test(self, symbol: str, side: str, type: str, **kwargs):
    """
    |
    | **New Test Order (TRADE)**
    | *Send a new test order*
    :API endpoint: ``POST /fapi/v1/order/test``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#new-order-trade
    :parameter symbol: string
    :parameter side: string
    :parameter type: string
    :parameter positionSide: optional string. async default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be passed in Hedge Mode.
    :parameter timeInForce: optional string
    :parameter quantity: optional float
    :parameter reduceOnly: optional string
    :parameter price: optional float
    :parameter newClientOrderId: optional string. An unique ID among open orders. Automatically generated if not sent.
    :parameter stopPrice: optional float. Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter closePosition: optional string. true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
    :parameter activationPrice: optional float. Use with TRAILING_STOP_MARKET orders, async default is the latest price (supporting different workingType).
    :parameter callbackRate: optional float. Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
    :parameter workingType: optional string. stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". async default "CONTRACT_PRICE".
    :parameter priceProtect: optional string. "TRUE" or "FALSE", async default "FALSE". Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter newOrderRespType: optional float. "ACK" or "RESULT", async default "ACK".

    |
    """
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/fapi/v1/order/test"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, **params)


async def new_batch_order(self, batch_orders: list):
    """
    |
    | **Place Multiple Orders (TRADE)**
    | *Post a new batch order*
    :API endpoint: ``POST /fapi/v1/batchOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade
    :parameter symbol: string
    :parameter side: string
    :parameter type: string
    :parameter positionSide: optional string. async default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be passed in Hedge Mode.
    :parameter timeInForce: optional string
    :parameter quantity: optional float
    :parameter reduceOnly: optional string
    :parameter price: optional float
    :parameter newClientOrderId: optional string. An unique ID among open orders. Automatically generated if not sent.
    :parameter stopPrice: optional float. Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter closePosition: optional string. true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
    :parameter activationPrice: optional float. Use with TRAILING_STOP_MARKET orders, async default is the latest price (supporting different workingType).
    :parameter callbackRate: optional float. Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
    :parameter workingType: optional string. stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". async default "CONTRACT_PRICE".
    :parameter priceProtect: optional string. "TRUE" or "FALSE", async default "FALSE". Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter newOrderRespType: optional float. "ACK" or "RESULT", async default "ACK".

    |
    **Notes**
        - Batch orders are processed concurrently, and the order of matching is not guaranteed.
        - The order of returned contents for batch orders is the same as the order of the order list.
            - batchOrders (list): order list. Max 5 orders
        - batchOrders is the list of order parameters in JSON
        - example:
                batch_orders = [
                    {
                        "symbol":"BTCUSDT",
                        "side": "SELL",
                        "type": "LIMIT",
                        "quantity": "0.001",
                        "timeInForce": "GTC",
                        "reduceOnly": "false",
                        "price": "9563.51"
                    },
                    {
                        "symbol":"BTCUSDT",
                        "side": "SELL",
                        "type": "LIMIT",
                        "quantity": "0.001",
                        "timeInForce": "GTC",
                        "reduceOnly": "false",
                        "price": "9613.51"
                    }
                ]
    |
    """
    url_path = "/fapi/v1/batchOrders"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, batchOrders=ujson.dumps(batch_orders))


async def query_order(self, symbol: str, order_id: int | str):
    """
    |
    | **Query Order (USER_DATA)**
    | *Check an order's status*
    :API endpoint: ``GET /fapi/v1/order``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#query-order-user_data
    :parameter symbol: string
    :parameter order_id: int orderId or string origClientOrderId
    |
    """

    if isinstance(order_id, int):
        params = {"symbol": symbol, "orderId": order_id}
    else:
        params = {"symbol": symbol, "origClientOrderId": order_id}

    url_path = "/fapi/v1/order"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, **params)


async def cancel_order(self, symbol: str, order_id: int | str):
    """
    |
    | **Cancel Order (TRADE)**
    | *Cancel an active order.*
    :API endpoint: ``DELETE /fapi/v1/order``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#cancel-order-trade
    :parameter symbol: string
    :parameter order_id: int orderId or string origClientOrderId
    |
    """

    if isinstance(order_id, int):
        params = {"symbol": symbol, "orderId": order_id}
    else:
        params = {"symbol": symbol, "origClientOrderId": order_id}

    url_path = "/fapi/v1/order"
    return await self._fetch(True, 'DELETE', sys._getframe().f_code.co_name, url_path, **params)


async def cancel_open_orders(self, symbol: str):
    """
    |
    | **Cancel All Open Orders (TRADE)**
    :API endpoint: ``DELETE /fapi/v1/allOpenOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#cancel-all-open-orders-trade
    :parameter symbol: string
    |
    """
    url_path = "/fapi/v1/allOpenOrders"
    return await self._fetch(True, 'DELETE', sys._getframe().f_code.co_name, url_path, symbol=symbol)


async def cancel_batch_order(self, symbol: str, order_id_list: list[int | str]):
    """
    |
    | **Cancel Multiple Orders (TRADE)**
    | *Cancel a new batch order*
    :API endpoint: ``DELETE /fapi/v1/batchOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#cancel-multiple-orders-trade
    :parameter symbol: string
    :parameter order_id_list: int list; max length 10 e.g. [1234567, 2345678] or string list; max length 10 e.g. ["my_id_1", "my_id_2"], encode the double quotes. No space after comma.
    **Notes**
        - Either orderIdList or origClientOrderIdList must be sent.
    |
    """

    url_path = "/fapi/v1/batchOrders"
    if isinstance(order_id_list[0], int):
        params = {"symbol": symbol, "orderIdList": ujson.dumps(order_id_list)}
    else:
        params = {"symbol": symbol,
                  "origClientOrderIdList": ujson.dumps(order_id_list)}

    return await self._fetch(True, 'DELETE', sys._getframe().f_code.co_name, url_path, **params)


async def countdown_cancel_order(self, symbol: str, countdownTime: int):
    """
    |
    | **Auto-Cancel All Open Orders (TRADE)**
    | *Cancel all open orders of the specified symbol at the end of the specified countdown.*
    :API endpoint: ``POST /fapi/v1/countdownCancelAll``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#auto-cancel-all-open-orders-trade
    :parameter symbol: string
    :parameter countdownTime: int list; countdown time, 1000 for 1 second. 0 to cancel the timer.
    **Notes**
        - The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and replaced by a new one.
        - Example usage:
            - Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).
            - If this endpoint is not called within 120 seconds, all your orders of the specified symbol will be automatically canceled.
            - If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.
        - The system will check all countdowns approximately every 10 milliseconds, so please note that sufficient redundancy should be considered when using this function. 
        - We do not recommend setting the countdown time to be too precise or too small.
    """
    url_path = "/fapi/v1/countdownCancelAll"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, symbol=symbol, countdownTime=countdownTime)


async def get_open_orders(self, symbol: str, order_id: int | str):
    """
    |
    | **Query Current Open Order (USER_DATA)**
    | *Get all open orders on a symbol.*
    :API endpoint: ``GET /fapi/v1/openOrder``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#query-current-open-order-user_data
    :parameter symbol: string
    :parameter orderId: optional int
    :parameter origClientOrderId: optional int

    **Notes**
        - Either orderId or origClientOrderId must be sent
        - If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
    """

    url_path = "/fapi/v1/openOrder"
    if isinstance(order_id, int):
        params = {"symbol": symbol, "orderId": order_id}
    else:
        params = {"symbol": symbol, "origClientOrderId": order_id}

    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, **params)


async def get_orders(self, symbol: str = None):
    """
    |
    | **Current All Open Orders (USER_DATA)**
    | *Get all open orders on a symbol. Careful when accessing this with no symbol.*
    | *If the symbol is not sent, orders for all symbols will be returned in an array.*
    :API endpoint: ``GET /fapi/v1/openOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#current-all-open-orders-user_data
    :parameter symbol: optional string
    |
    """
    url_path = "/fapi/v1/openOrders"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, symbol=symbol)


async def get_all_orders(self, symbol: str, **kwargs):
    """
    |
    | **All Orders (USER_DATA)**
    | *Get all account orders; active, canceled, or filled.*
    :API endpoint: ``GET /fapi/v1/allOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#all-orders-user_data
    :parameter symbol: string
    :parameter orderId: optional int
    :parameter startTime: optional int
    :parameter endTime: optional int
    :parameter limit: optional int
    |
    """
    url_path = "/fapi/v1/allOrders"
    params = {"symbol": symbol, **kwargs}
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, **params)


async def balance(self):
    """
    |
    | **Futures Account Balance V2 (USER_DATA)**
    | *Get current account balance*
    :API endpoint: ``GET /fapi/v2/balance``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#futures-account-balance-v2-user_data
    |
    """

    url_path = "/fapi/v2/balance"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path)


async def account(self):
    """
    |
    | **Account Information V2 (USER_DATA)**
    | *Get current account information*
    :API endpoint: ``GET /fapi/v2/account``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#account-information-v2-user_data

    |
    """

    url_path = "/fapi/v2/account"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path)


async def change_leverage(self, symbol: str, leverage: int):
    """
    |
    | **Change Initial Leverage (TRADE)**
    | *Change user's initial leverage of specific symbol market.*
    :API endpoint: ``POST /fapi/v1/leverage``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#change-initial-leverage-trade
    :parameter symbol: string
    :parameter leverage: int; target initial leverage: int from 1 to 125.
    |
    """
    url_path = "/fapi/v1/leverage"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, symbol=symbol, leverage=leverage)


async def change_margin_type(self, symbol: str, marginType: str):
    """
    |
    | **Change margin type (TRADE)**
    | *Change user's margin type of specific symbol market.*
    :API endpoint: ``POST /fapi/v1/marginType``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#change-margin-type-trade
    :parameter symbol: string
    :parameter marginType: string; ISOLATED, CROSSED.
    |
    """
    url_path = "/fapi/v1/marginType"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, symbol=symbol, marginType=marginType)


async def modify_isolated_position_margin(self, symbol: str, amount: float, type: int, **kwargs):
    """
    |
    | **Modify Isolated Position Margin (TRADE)**
    :API endpoint: ``POST /fapi/v1/positionMargin``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#modify-isolated-position-margin-trade
    :parameter symbol: string
    :parameter amount: float
    :parameter type: int; 1: Add position margin, 2: Reduce position margin
    :parameter positionSide: optional string; async default BOTH for One-way Mode, LONG or SHORT for Hedge Mode. It must be sent with Hedge Mode.
    |
    """
    url_path = "/fapi/v1/positionMargin"
    params = {"symbol": symbol, "amount": amount, "type": type, **kwargs}
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path, **params)


async def get_position_margin_history(self, symbol: str, **kwargs):
    """
    |
    | **Get Position Margin Change History (TRADE)**
    | *Get position margin history on a symbol.*
    :API endpoint: ``GET /fapi/v1/positionMargin/history``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-position-margin-change-history-trade
    :parameter symbol: string
    :parameter type: optional int; 1: Add position margin, 2: Reduce position margin.
    :parameter startTime: optional int
    :parameter endTime: optional int
    :parameter limit: optional int; async default: 500.

    |
    """
    url_path = "/fapi/v1/positionMargin/history"
    params = {"symbol": symbol, **kwargs}

    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, **params)


async def get_position_risk(self, symbol: str = None):
    """
    |
    | **Position Information V2 (USER_DATA)**
    | *Get current position information.*
    :API endpoint: ``GET /fapi/v2/positionRisk``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#position-information-v2-user_data
    :parameter symbol: string

    |
    """

    url_path = "/fapi/v2/positionRisk"

    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, symbol=symbol)


async def get_account_trades(self, symbol: str, **kwargs):
    """
    |
    | **Account Trade List (USER_DATA)**
    | *Get trades for a specific account and symbol.*
    :API endpoint: ``GET /fapi/v1/userTrades``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#account-trade-list-user_data
    :parameter symbol: string
    :parameter startTime: optional int
    :parameter endTime: optional int
    :parameter fromId: optional int; trade ID to fetch from, async default gets most recent trades.
    :parameter limit: optional int; async default: 500, max: 1000.

    **Notes**
        - If startTime and endTime are both not sent, then the last 7 days' data will be returned.
        - The time between startTime and endTime cannot be longer than 7 days.
        - The parameter fromId cannot be sent with startTime or endTime.
    |
    """

    url_path = "/fapi/v1/userTrades"
    params = {"symbol": symbol, **kwargs}

    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, **params)


async def get_income_history(self, kwargs):
    """
    |
    | **Get Income History (USER_DATA)**
    | *Get trades for a specific account and symbol.*
    :API endpoint: ``GET /fapi/v1/income``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-income-history-user_data
    :parameter symbol: optional string
    :parameter incomeType: optional string; "TRANSFER", "WELCOME_BONUS", "REALIZED_PNL", "FUNDING_FEE", "COMMISSION" and "INSURANCE_CLEAR".
    :parameter startTime: optional int; timestamp in ms to get funding from INCLUSIVE.
    :parameter endTime: optional int; timestamp in ms to get funding from INCLUSIVE.
    :parameter limit: optional int; async default: 100, max: 1000.

    **Notes**
        - If neither startTime nor endTime is sent, the recent 7-day data will be returned.
        - If incomeType is not sent, all kinds of flow will be returned
        - "trandId" is unique in the same incomeType for a user
    """

    url_path = "/fapi/v1/income"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, kwargs)


async def leverage_brackets(self, kwargs):
    """
    |
    | **Notional and Leverage Brackets (USER_DATA)**
    | *Get notional and leverage bracket.*
    :API endpoint: ``GET /fapi/v1/leverageBracket``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#notional-and-leverage-brackets-user_data
    :parameter symbol: optional string

    |
    """

    url_path = "/fapi/v1/leverageBracket"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, kwargs)


async def adl_quantile(self, kwargs):
    """
    |
    | **Position ADL Quantile Estimation (USER_DATA)**
    | *Get Position ADL Quantile Estimation*
    :API endpoint: ``GET /fapi/v1/adlQuantile``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#position-adl-quantile-estimation-user_data
    :parameter symbol: optional string

    **Notes**
        - Values update every 30s.
        - Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
        - For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
        - If the positions of the symbol are crossed margined in Hedge Mode:
            - "HEDGE" as a sign will be returned instead of "BOTH"
        - A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
    |
    """

    url_path = "/fapi/v1/adlQuantile"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, kwargs)


async def force_orders(self, kwargs):
    """
    |
    | **User's Force Orders (USER_DATA)**
    | *Get User's Force Orders*
    :API endpoint: ``GET /fapi/v1/forceOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#user-39-s-force-orders-user_data
    :parameter symbol: optional string
    :parameter autoCloseType: optional string; "LIQUIDATION" for liquidation orders, "ADL" for ADL orders.
    :parameter startTime: optional int
    :parameter endTime: optional int
    :parameter Limit: optional int; async default 50, max 100.

    **Notes**
        - If "autoCloseType" is not sent, orders with both of the types will be returned
        - If "startTime" is not sent, data within 7 days before "endTime" can be queried
    |
    """

    url_path = "/fapi/v1/forceOrders"

    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, kwargs)


async def api_trading_status(self, kwargs):
    """
    |
    | **User API Trading Quantitative Rules Indicators (USER_DATA)**
    | *Get User API Trading Quantitative Rules Indicators*
    :API endpoint: ``GET /fapi/v1/apiTradingStatus``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#user-api-trading-quantitative-rules-indicators-user_data
    :parameter symbol: optional string

    |
    """

    url_path = "/fapi/v1/apiTradingStatus"

    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, kwargs)


async def commission_rate(self, symbol: str):
    """
    |
    | **User Commission Rate (USER_DATA)**
    | *Get commission rate of symbol*
    :API endpoint: ``GET /fapi/v1/commissionRate``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#user-commission-rate-user_data
    :parameter symbol: string

    |
    """
    url_path = "/fapi/v1/commissionRate"
    return await self._fetch(True, 'GET', sys._getframe().f_code.co_name, url_path, symbol=symbol)
