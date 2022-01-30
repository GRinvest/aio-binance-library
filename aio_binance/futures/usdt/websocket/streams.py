

class Streams:

    async def stream_agg_trade(self,
                               symbol: str,
                               callback_event: object = None) -> str | dict:
        """**Aggregate Trade Streams**
            The Aggregate Trade Streams push market trade information
            that is aggregated for a single taker order every 100 milliseconds.

            Only market trades will be aggregated,
            which means the insurance fund trades and ADL trades won't be aggregated.
        **Stream Name:**
            <symbol>@aggTrade
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#aggregate-trade-streams
        Args:
            symbol: the trading symbol.
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Notes:
            Update Speed: 100ms
        """
        stream = f"{symbol.lower()}@aggTrade"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_mark_price(self,
                                symbol: str,
                                callback_event: object = None) -> str | dict:
        """**Mark Price Streams**
            Mark price and funding rate for all symbols pushed every 3 seconds or every second.
        **Stream Name:**
            <symbol>@markPrice@1s
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#mark-price-stream
        Args:
            symbol: the trading symbol.
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        """
        stream = f"{symbol.lower()}@markPrice@1s"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_kline(self,
                           symbol: str,
                           interval: str,
                           callback_event: object = None) -> str | dict:
        """**Kline/Candlestick Streams**
            The Kline/Candlestick Stream push updates to the current klines/candlestick
            every 250 milliseconds (if existing)
        **Stream Name:**
            <symbol>@kline_<interval>
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-streams
        Args:
            symbol: the trading symbol.
            interval: m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Examples:
            interval:
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
        Notes:
            Update Speed: 250ms
        """
        stream = f"{symbol.lower()}@kline_{interval}"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_continuous_kline(self,
                                      symbol: str,
                                      contract_type: str,
                                      interval: str,
                                      callback_event: object = None) -> str | dict:
        """**Continuous Kline/Candlestick Streams**
            The Kline/Candlestick Stream push updates to Kline/candlestick bars for a specific contract type.
            every 250 milliseconds
        **Stream Name:**
            <symbol>_<contract_type>@continuousKline_<interval>
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-streams
        Args:
            symbol: the trading symbol.
            contract_type: perpetual, current_quarter, next_quarter
            interval: m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Examples:
            interval:
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
        Notes:
            Update Speed: 250ms
        """
        stream = f"{symbol.lower()}_{contract_type}@continuousKline_{interval}"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_mini_ticker(self,
                                 symbol: str = None,
                                 callback_event: object = None) -> str | dict:
        """**Individual symbol or all symbols mini ticker**
            24hr rolling window mini-ticker statistics.
            These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs
        **Stream Name:**
            <symbol>@miniTicker or !miniTicker@arr
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#individual-symbol-mini-ticker-stream

            https://binance-docs.github.io/apidocs/futures/en/#individual-symbol-ticker-streams
        Args:
            symbol: the trading symbol or None.
                if None 24hr rolling window mini-ticker statistics for all symbols. Default: None
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Notes:
            Update Speed: 500ms for individual symbol, 1000ms for all market symbols
        """
        stream = "!miniTicker@arr" if symbol is None else f"{symbol.lower()}@miniTicker"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_ticker(self,
                            symbol=None,
                            callback_event: object = None) -> str | dict:
        """**Individual symbol or all symbols ticker**
            24hr rolling window ticker statistics for a single symbol.

            These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.
        **Stream Name:**
            <symbol>@ticker or !ticker@arr
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#individual-symbol-ticker-streams

            https://binance-docs.github.io/apidocs/futures/en/#all-market-tickers-streams
        Args:
            symbol: the trading symbol or None.
                if None 24hr rolling window ticker statistics for all symbols. Default: None
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Notes:
            Update Speed: 500ms for individual symbol, 1000ms for all market symbols
        """
        stream = "!ticker@arr" if symbol is None else f"{symbol.lower()}@ticker"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_book_ticker(self,
                                 symbol=None,
                                 callback_event: object = None) -> str | dict:
        """**Individual symbol or all book ticker**
            Pushes any update to the best bid or asks price or quantity in real-time for a specified symbol.
        **Stream Name:**
            <symbol>@bookTicker or !bookTicker
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#individual-symbol-book-ticker-streams

            https://binance-docs.github.io/apidocs/futures/en/#all-book-tickers-stream
        Args:
            symbol: the trading symbol or None.
                if None 24hr rolling window book-ticker statistics for all symbols. Default: None
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Notes:
            Update Speed: Real-time
        """
        stream = "!bookTicker" if symbol is None else f"{symbol.lower()}@bookTicker"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_liquidation_order(self,
                                       symbol=None,
                                       callback_event: object = None) -> str | dict:
        """**The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol.**
            The Liquidation Order Snapshot Streams push force
            liquidation order information for all symbols in the market.

            For each symbol，only the latest one liquidation order
            within 1000ms will be pushed as the snapshot.
            If no liquidation happens in the interval of 1000ms, no stream will be pushed.

        **Stream Name:**
            <symbol>@forceOrder or !forceOrder@arr
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#liquidation-order-streams

            https://binance-docs.github.io/apidocs/futures/en/#all-market-liquidation-order-streams
        Args:
            symbol: the trading symbol or None.
                if None 24hr rolling window Liquidation Order statistics for all symbols. Default: None
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Notes:
            Update Speed: 1000ms
        """
        stream = "!forceOrder@arr" if symbol is None else f"{symbol.lower()}@forceOrder"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_partial_book_depth(self,
                                        symbol: str,
                                        level: int = 5,
                                        speed: int = 500,
                                        callback_event: object = None) -> str | dict:
        """**Partial Book Depth Streams**
            Top bids and asks,
        **Stream Names:**
            <symbol>@depth<levels>@<speed>ms
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#partial-book-depth-streams
        Args:
            symbol: the trading symbol.
            level: Valid are 5, 10, or 20. Default: 5.
            speed: 100ms, 250ms or 500ms. Default: 500
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams.
        """
        stream = f"{symbol.lower()}@depth{level}@{speed}ms"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_diff_book_depth(self,
                                     symbol: str,
                                     speed: int = 500,
                                     callback_event: object = None) -> str | dict:
        """**Diff. Depth Stream**
            Order book price and quantity depth updates used to locally manage an order book.
        **Stream Name:**
            <symbol>@depth@<speed>ms
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#diff-book-depth-streams
        Args:
            symbol: the trading symbol.
            speed: 100ms, 250ms or 500ms. Default: 500
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams.
        """
        stream = f"{symbol.lower()}@depth@{speed}ms"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_blvt_info(self,
                               symbol: str,
                               callback_event: object = None) -> str | dict:
        """**Blvt Info Stream**
            Get leverage token info
        **Stream Name:**
            <tokenName>@tokenNav
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#blvt-info-streams
        Args:
            symbol: the trading symbol.
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams.
        """
        stream = f"{symbol.upper()}@tokenNav"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_blvt_kline(self,
                                symbol: str,
                                interval: str,
                                callback_event: object = None) -> str | dict:
        """**BLVT Kline/Candlestick Streams**
            The Kline/Candlestick Stream push updates to the current
            klines/candlestick every 300 milliseconds (if existing)
        **Stream Name:**
            <tokenName>@nav_Kline_<interval>
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#blvt-nav-kline-candlestick-streams
        Args:
            symbol: the trading symbol.
            interval: m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Examples:
            interval:
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
        Notes:
            Update Speed: 300ms
        """
        stream = f"{symbol.upper()}@nav_Kline_{interval}"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_composite_index(self,
                                     symbol: str,
                                     callback_event: object = None) -> str | dict:
        """**Composite Index Info Stream**
            Composite index information for index symbols pushed every second.
        **Stream Name:**
            <symbol>@compositeIndex
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information-streams
        Args:
            symbol: the trading symbol.
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Notes:
            Update Speed: 1000ms
        """
        stream = f"{symbol.lower()}@compositeIndex"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def stream_user_data(self, callback_event: object = None) -> str | dict:
        """**listen to user data by provided listen key**

        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#user-data-streams
        Args:
            callback_event: Custom function where websocket messages will be processed. Default None
                If callback_event None, then the websocket will not connect,
                and the response will return the string value of the stream.
                Can be used to connect to multiple streams
        Notes:
            - A User Data Stream listenKey is valid for 60 minutes after creation.
            - Doing a client.update_private_listen_key() on a listenKey will extend its validity for 60 minutes.
            - Doing a client.delete_private_listen_key() on a listenKey will close the stream
                and invalidate the listenKey.
            - Doing a client.create_private_listen_key() on an account with an active listenKey
                will return the currently active listenKey and extend its validity for 60 minutes.
            - A single connection is only valid for 24 hours; expect to be disconnected at the 24-hour mark
        **Events:**
            **User Data Stream Expired:**
                When the listenKey used for the user data stream turns expired, this event will be pushed.

                **Notes:**
                    - This event is not related to the websocket disconnection.
                    - This event will be received only when a valid listenKey in connection got expired.
                    - No more user data event will be updated after this event received until a new valid listenKey used.
                **Event Type:**
                    {"e":"listenKeyExpired"}
            **Margin Call:**
                - When the user's position risk ratio is too high, this stream will be pushed.
                - This message is only used as risk guidance information and is not recommended for investment strategies.
                - In the case of a highly volatile market, there may be the possibility
                that the user's position has been liquidated at the same time when this stream is pushed out.

                **Event Type:**
                    {"e":"MARGIN_CALL"}
            **Balance and Position Update:**
                **Event Type:**
                    {"e":"ACCOUNT_UPDATE"}
            **Order Update:**
                When new order created, order status changed will push such event. event type is ORDER_TRADE_UPDATE.
            **Account Configuration Update previous Leverage Update:**
                When the account configuration is changed, the event type will be pushed as ACCOUNT_CONFIG_UPDATE
        """
        stream = "listenKey"
        if callback_event is None:
            return stream
        await self._listen_forever(stream, callback_event)

    async def subscription_streams(self,
                                   streams: list[str],
                                   callback_event: object = None) -> dict:
        """ **Creates multiple streams from the arguments passed to it**

        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#websocket-market-streams
        Args:
            streams: List[str]
            callback_event: Custom function where websocket messages will be processed.
        """
        stream = 'streams='+'/'.join(streams)
        await self._listen_forever(stream, callback_event)
