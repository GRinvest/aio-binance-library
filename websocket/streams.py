

async def agg_trade(self, symbol: str, callback_event: object=None):
    """Aggregate Trade Streams
    The Aggregate Trade Streams push market trade information that is aggregated for a single taker order every 100 milliseconds.
    Only market trades will be aggregated, which means the insurance fund trades and ADL trades won't be aggregated.
    
    Stream Name: <symbol>@aggTrade
    https://binance-docs.github.io/apidocs/futures/en/#aggregate-trade-streams
    Update Speed: 100ms
    """
    stream = f"{symbol.lower()}@aggTrade"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def mark_price(self, symbol: str, callback_event: object=None):
    """Mark Price Streams
    Mark price and funding rate for all symbols pushed every 3 seconds or every second.
    
    Stream Name: <symbol>@markPrice or <symbol>@markPrice@1s
    https://binance-docs.github.io/apidocs/futures/en/#mark-price-stream
    """
    stream = f"{symbol.lower()}@markPrice@1s"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def kline(self, symbol: str, interval: str, callback_event: object=None):
    """Kline/Candlestick Streams
    The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing)
    Stream Name: <symbol>@kline_<interval>
    https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-streams
    interval:
    m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
    - 1m
    - 3m
    - 5m
    - 15m
    - 30m
    - 1h
    - 2h
    - 4h
    - 6h
    - 8h
    - 12h
    - 1d
    - 3d
    - 1w
    - 1M
    Update Speed: 250ms
    """
    stream = f"{symbol.lower()}@kline_{interval}"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)


async def continuous_kline(self, pair: str, contractType: str, interval: str, callback_event: object=None):
    """Continuous Kline/Candlestick Streams
    The Kline/Candlestick Stream push updates to Kline/candlestick bars for a specific contract type. every 250 milliseconds
    Stream Name: <pair>_<contractType>@continuousKline_<interval>
    https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-streams
    interval:
    m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
    - 1m
    - 3m
    - 5m
    - 15m
    - 30m
    - 1h
    - 2h
    - 4h
    - 6h
    - 8h
    - 12h
    - 1d
    - 3d
    - 1w
    - 1M
    Update Speed: 250ms
    """
    stream = f"{pair.lower()}_{contractType}@continuousKline_{interval}"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)


async def mini_ticker(self, symbol=None, callback_event: object=None):
    """Individual symbol or all symbols mini ticker
    24hr rolling window mini-ticker statistics.
    These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs
    Stream Name: <symbol>@miniTicker or
    Stream Name: !miniTicker@arr
    https://binance-docs.github.io/apidocs/futures/en/#individual-symbol-mini-ticker-stream
    https://binance-docs.github.io/apidocs/futures/en/#individual-symbol-ticker-streams
    Update Speed: 500ms for individual symbol, 1000ms for all market symbols
    """
    if symbol is None:
        stream = "!miniTicker@arr"
    else:
        stream = f"{symbol.lower()}@miniTicker"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def ticker(self, symbol=None, callback_event: object=None):
    """Individual symbol or all symbols ticker
    24hr rolling window ticker statistics for a single symbol.
    These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.
    Stream Name: <symbol>@ticker or
    Stream Name: !ticker@arr
    https://binance-docs.github.io/apidocs/futures/en/#individual-symbol-ticker-streams
    https://binance-docs.github.io/apidocs/futures/en/#all-market-tickers-streams
    Update Speed: 500ms for individual symbol, 1000ms for all market symbols
    """

    if symbol is None:
        stream = "!ticker@arr"
    else:
        stream = f"{symbol.lower()}@ticker"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def book_ticker(self, symbol=None, callback_event: object=None):
    """Individual symbol or all book ticker
    Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.
    Stream Name: <symbol>@bookTicker or
    Stream Name: !bookTicker
    https://binance-docs.github.io/apidocs/futures/en/#individual-symbol-book-ticker-streams
    https://binance-docs.github.io/apidocs/futures/en/#all-book-tickers-stream
    
    Update Speed: Real-time
    """
    if symbol is None:
        stream = "!bookTicker"
    else:
        stream = f"{symbol.lower()}@bookTicker"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def liquidation_order(self, symbol=None, callback_event: object=None):
    """The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol.
    The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market.
    For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.
    
    Stream Name: <symbol>@forceOrder or 
    Stream Name: !forceOrder@arr
    https://binance-docs.github.io/apidocs/futures/en/#liquidation-order-streams
    https://binance-docs.github.io/apidocs/futures/en/#all-market-liquidation-order-streams
    
    Update Speed: 1000ms
    """
    if symbol is None:
        stream = "!forceOrder@arr"
    else:
        stream = f"{symbol.lower()}@forceOrder"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def partial_book_depth(self, symbol: str, level: int=5, speed: int=500, callback_event: object=None):
    """Partial Book Depth Streams
    Top bids and asks, Valid are 5, 10, or 20.
    Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@500ms OR <symbol>@depth<levels>@100ms
    https://binance-docs.github.io/apidocs/futures/en/#partial-book-depth-streams
    Update Speed: 250ms, 500ms or 100ms
    """
    stream = f"{symbol.lower()}@depth{level}@{speed}ms"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def diff_book_depth(self, symbol: str, speed: int, callback_event: object=None):
    """Diff. Depth Stream
    Order book price and quantity depth updates used to locally manage an order book.
    Stream Name: <symbol>@depth OR <symbol>@depth@500ms OR<symbol>@depth@100ms
    https://binance-docs.github.io/apidocs/futures/en/#diff-book-depth-streams
            
    Update Speed: 250ms, 500ms or 100ms
    """
    stream = f"{symbol.lower()}@depth@{speed}ms"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def blvt_info(self, symbol: str, callback_event: object=None):
    """Blvt Info Stream
    get leverage token info
    Stream Name: <tokenName>@tokenNav
    https://binance-docs.github.io/apidocs/futures/en/#blvt-info-streams
    """
    stream = f"{symbol.upper()}@tokenNav"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def blvt_kline(self, symbol: str, interval: str, callback_event: object=None):
    """BLVT Kline/Candlestick Streams
    The Kline/Candlestick Stream push updates to the current klines/candlestick every 300 milliseconds (if existing)
    Stream Name: <tokenName>@nav_Kline_<interval>
    https://binance-docs.github.io/apidocs/futures/en/#blvt-nav-kline-candlestick-streams
    interval:
    m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
    - 1m
    - 3m
    - 5m
    - 15m
    - 30m
    - 1h
    - 2h
    - 4h
    - 6h
    - 8h
    - 12h
    - 1d
    - 3d
    - 1w
    - 1M
    Update Speed: 300ms
    """
    stream = f"{symbol.upper()}@nav_Kline_{interval}"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def composite_index(self, symbol: str, callback_event: object=None):
    """Composite Index Info Stream
    Composite index information for index symbols pushed every second.
    Stream Name: <symbol>@compositeIndex
    https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information-streams
    
    Update Speed: 1000ms
    """
    stream = f"{symbol.lower()}@compositeIndex"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def user_data(self, callback_event: object=None):
    """listen to user data by provided listenkey"""
    stream = "listenKey"
    if callback_event is None:
        return stream
    await self._listen_forever(stream, callback_event)

async def subscription_streams(self, streams: list, callback_event: object):
    stream = 'streams='+'/'.join(streams)
    await self._listen_forever(stream, callback_event)
