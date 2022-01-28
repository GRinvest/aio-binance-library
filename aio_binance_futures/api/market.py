import sys

async def ping(self):
    """
    |
    | **Test Connectivity**
    | *Test connectivity to the Rest API.*
    :API endpoint: ``GET /fapi/v1/ping``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#test-connectivity
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/ping")


async def time(self):
    """
    |
    | **Check Server Time**
    | *Test connectivity to the Rest API and get the current server time.*
    :API endpoint: ``GET /fapi/v1/time``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#check-server-time
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/time")


async def exchange_info(self) -> dict:
    """
    **Exchange Information**\n
    *Current exchange trading rules and symbol information.*\n
    :API endpoint: ``GET /fapi/v1/exchangeInfo``\n
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#exchange-information\n

    Returns:
        dict: Exchange Information
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/exchangeInfo")


async def depth(self, symbol: str, **kwargs):
    """
    |
    | **Get Orderbook**
    :API endpoint: ``GET /fapi/v1/depth``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#order-book
    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. async default 500, valid limits: [5, 10, 20, 50, 100, 500, 1000].
    |
    """
    params = {"symbol": symbol, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/depth", **params)


async def trades(self, symbol: str, **kwargs):
    """
    |
    | **Get Recent Market Trades**
    :API endpoint: ``GET /fapi/v1/trades``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list
    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. async default 500, max 1000.
    |
    """
    params = {"symbol": symbol, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/trades", **params)


async def historical_trades(self, symbol: str, **kwargs):
    """
    |
    | **Old Trade Lookup**
    | *Get older market historical trades.*
    :API endpoint: ``GET /fapi/v1/historicalTrades``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#old-trades-lookup-market_data
    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. async default 500, max 1000.
    :parameter formId: optional int; trade ID to fetch from. async default gets most recent trades.
    |
    """
    params = {"symbol": symbol, **kwargs}
    return self.limit_request("GET", "/fapi/v1/historicalTrades", **params)


async def agg_trades(self, symbol: str, **kwargs):
    """
    |
    | **Compressed/Aggregate Trades List**
    | *Get compressed, aggregate market trades. Market trades that fill at the time, from the same order, with the same price will have the quantity aggregated.*
    
    :API endpoint: ``GET /fapi/v1/aggTrades``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list
    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. async default 500, max 1000.
    :parameter formId: optional int; ID to get aggregate trades from INCLUSIVE.
    :parameter startTime: optional int; timestamp in ms to get aggregate trades from INCLUSIVE.
    :parameter endTime: optional int; timestamp in ms to get aggregate trades from INCLUSIVE.
    |
    """
    params = {"symbol": symbol, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/aggTrades", **params)


async def klines(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Kline/Candlestick Data**
    | *Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.*
    :API endpoint: ``GET /fapi/v1/klines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data
    :parameter symbol: string; the trading symbol.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. async default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    |
    """
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/klines", **params)


async def continuous_klines(self, pair: str, contractType: str, interval: str, **kwargs):
    """
    |
    | **Continuous Kline/Candlestick Data**
    | *Kline/candlestick bars for a specific contract type. Klines are uniquely identified by their open time.*  
    
    :API endpoint: ``GET /fapi/v1/continuousKlines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-data
    :parameter pair: string; the trading pair.
    :parameter contractType: string; PERPETUAL, CURRENT_MONTH, NEXT_MONTH, CURRENT_QUARTER, NEXT_QUARTER.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. async default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    |
    """
    params = {"pair": pair, "contractType":contractType, "interval": interval, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/continuousKlines", **params)


async def index_price_klines(self, pair: str, interval: str, **kwargs):
    """
    |
    | **Kline/Candlestick Data for the index price of a pair.**
    | *Klines are uniquely identified by their open time.*   
    
    :API endpoint: ``GET /fapi/v1/indexPriceKlines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#index-price-kline-candlestick-data
    :parameter pair: string; the trading pair.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. async default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    |
    """
    params = {"pair": pair, "interval": interval, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/indexPriceKlines", **params)


async def mark_price_klines(self, symbol: str, interval: str, **kwargs) -> list:
    """
    |
    | **Kline/candlestick bars for the mark price of a symbol.**\n
    | *Klines are uniquely identified by their open time.*\n
    
    :API endpoint: ``GET /fapi/v1/markPriceKlines``\n
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#mark-price-kline-candlestick-data\n

    Args:
        symbol (str): the trading symbol.\n
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)\n
        limit optional(int): limit the results. async default 500, max 1000.\n
        startTime optional(int)\n
        endTime: optional(int)\n

    Returns:
        [list]: Kline/candlestick bars List
    """
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/markPriceKlines", **params)


async def mark_price(self, symbol: str):
    """
    |
    | **Mark Price and Funding Rate**
    :API endpoint: ``GET /fapi/v1/premiumIndex``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#mark-price
    :parameter symbol: string; the trading symbol.
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/premiumIndex", symbol=symbol)


async def funding_rate(self, symbol: str,  **kwargs):
    """
    |
    | **Funding Rate History
    :API endpoint: ``GET /fapi/v1/fundingRate``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history
    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. async default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    **Notes**
        - If startTime and endTime are not sent, the most recent limit datas are returned.
        - If the number of data between startTime and endTime is larger than limit, return as startTime + limit.
        - In ascending order.
    |
    """
    params = {"symbol": symbol, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/fundingRate", **params)


async def ticker_24hr_price_change(self, symbol: str = None):
    """
    |
    | **24 hour rolling window price change statistics.**
    | *Careful when accessing this with no symbol.*
    | *If the symbol is not sent, tickers for all symbols will be returned in an array.*
    :API endpoint: ``GET /fapi/v1/ticker/24hr``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#24hr-ticker-price-change-statistics
    :parameter symbol: string; the trading symbol.
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/ticker/24hr", symbol=symbol)


async def ticker_price(self, symbol: str = None):
    """
    |
    | **Latest price for a symbol or symbols.**
    :API endpoint: ``GET /fapi/v1/ticker/price``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#symbol-price-ticker
    :parameter symbol: optional string; the trading symbol.
    **Notes**
        - If the symbol is not sent, prices for all symbols will be returned in an array.
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/ticker/price", symbol=symbol)


async def book_ticker(self, symbol: str = None):
    """
    |
    | **Best price/qty on the order book for a symbol or symbols.**
    :API endpoint: ``GET /fapi/v1/ticker/bookTicker``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#symbol-order-book-ticker
    :parameter symbol: optional string; the trading symbol.
    
    **Notes**
        - If the symbol is not sent, bookTickers for all symbols will be returned in an array.
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/ticker/bookTicker", symbol=symbol)


async def open_interest(self, symbol: str):
    """
    |
    | **Get present open interest of a specific symbol.**
    :API endpoint: ``GET /fapi/v1/openInterest``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#open-interest
    :parameter symbol: string; the trading symbol.
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/ticker/bookTicker", symbol=symbol)


async def blvt_kline(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Get Historical BLVT NAV Kline**
    
    :API endpoint: ``GET /fapi/v1/lvtKlines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#historical-blvt-nav-kline-candlestick
    :parameter symbol: string; the trading symbol.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. async default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
    |
    """
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/lvtKlines", **params)


async def index_info(self, symbol: str = None):
    """
    |
    | **Get Index Composite**
    :API endpoint: ``GET /fapi/v1/indexInfo``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information
    :parameter symbol: optional string; the trading symbol.
    **Notes**
        - Only for composite index symbols.
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/indexInfo", symbol=symbol)


async def asset_Index(self, symbol: str = None):
    """
    |
    | **Get asset index for Multi-Assets mode**
    :API endpoint: ``GET /fapi/v1/assetIndex``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#multi-assets-mode-asset-index
    :parameter symbol: optional string; Asset pair in multi asset mode (ex: BTCUSD).
    |
    """
    return await self._fetch(False, 'GET', sys._getframe().f_code.co_name, "/fapi/v1/assetIndex", symbol=symbol)