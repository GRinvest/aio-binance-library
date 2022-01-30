

class Market:

    async def get_public_ping(self) -> None:
        """**Test connectivity to the Rest API.**

        Notes:
            ``GET /fapi/v1/ping``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#test-connectivity
        """
        return await self._fetch(
            'GET',
            'get_public_ping',
            "/fapi/v1/ping"
        )

    async def get_public_time(self) -> dict:
        """**Check Server Time**
            Test connectivity to the Rest API and get the current server time.

        Notes:
            ``GET /fapi/v1/time``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#check-server-time
        """
        return await self._fetch(
            'GET',
            'get_public_time',
            "/fapi/v1/time"
        )

    async def get_public_exchange_info(self) -> dict:
        """**Exchange Information**
            Current exchange trading rules and symbol information.

        Notes:
            ``GET /fapi/v1/exchangeInfo``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#exchange-information

        """
        return await self._fetch(
            'GET',
            'get_public_exchange_info',
            "/fapi/v1/exchangeInfo"
        )

    async def get_public_depth(self,
                               symbol: str,
                               limit: int = 500) -> dict:
        """**Get Orderbook**

        Notes:
            ``GET /fapi/v1/depth``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#order-book
        Args:
            symbol: the trading symbol.
            limit: Defaults 500, valid limits: [5, 10, 20, 50, 100, 500, 1000].
        """
        return await self._fetch(
            'GET',
            'get_public_depth',
            "/fapi/v1/depth",
            symbol=symbol,
            limit=limit
        )

    async def get_public_trades(self,
                                symbol: str,
                                limit: int = 500) -> dict:
        """**Get Recent Market Trades**

        Notes:
            ``GET /fapi/v1/trades``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list
        Args:
            symbol: the trading symbol.
            limit: limit the results. default 500, max 1000.
        |
        """
        return await self._fetch(
            'GET',
            'get_public_trades',
            "/fapi/v1/trades",
            symbol=symbol,
            limit=limit
        )

    async def get_public_historical_trades(self,
                                           symbol: str,
                                           **kwargs) -> list:
        """**Old Trade Lookup**
            Get older market historical trades.
        Notes:
            ``GET /fapi/v1/historicalTrades``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#old-trades-lookup-market_data
        Args:
            symbol: the trading symbol.
        Keyword Args:
            limit (int, optional): limit the results. default 500, max 1000.
            form_id (int, optional): trade ID to fetch from. default gets most recent trades.
        """
        return await self._fetch(
            "GET",
            'get_public_historical_trades',
            "/fapi/v1/historicalTrades",
            symbol=symbol,
            **self._to_api(kwargs)
        )

    async def get_public_agg_trades(self,
                                    symbol: str,
                                    **kwargs) -> list:
        """**Compressed/Aggregate Trades List**
            Get compressed, aggregate market trades.
            Market trades that fill at the time, from the same order,
            with the same price will have the quantity aggregated.

        Notes:
            ``GET /fapi/v1/aggTrades``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list
        Args:
            symbol: the trading symbol.
        Keyword Args:
            limit (Optional[int]): limit the results. default 500, max 1000.
            form_id (Optional[int]): ID to get aggregate trades from INCLUSIVE.
            start_time (Optional[int]): timestamp in ms to get aggregate trades from INCLUSIVE.
            end_time (Optional[int]): timestamp in ms to get aggregate trades from INCLUSIVE.
        """
        return await self._fetch(
            'GET',
            'get_public_agg_trades',
            "/fapi/v1/aggTrades",
            symbol=symbol,
            **self._to_api(kwargs)
        )

    async def get_public_klines(self,
                                symbol: str,
                                interval: str,
                                **kwargs) -> list:
        """**Kline/Candlestick Data**
            Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
        Notes:
            ``GET /fapi/v1/klines``
        See Also:
            - https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data,
            - the interval of kline see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info
        Args:
            symbol: the trading symbol.
            interval: the interval of kline, e.g. 1m, 5m, 1h, 1d, etc.
        Keyword Args:
            limit (Optional[int]): limit the results. async default 500, max 1000.
            start_time (Optional[int]): start time
            end_time (Optional[int]): end time
        """
        return await self._fetch(
            'GET',
            'get_public_klines',
            "/fapi/v1/klines",
            symbol=symbol,
            interval=interval,
            **self._to_api(kwargs)
        )

    async def get_public_continuous_klines(self,
                                           symbol: str,
                                           contract_type: str,
                                           interval: str,
                                           **kwargs) -> list:
        """**Continuous Kline/Candlestick Data**
            Kline/candlestick bars for a specific contract type.
            Klines are uniquely identified by their open time.
        Notes:
            ``GET /fapi/v1/continuousKlines``
        See Also:
            - Api doc: https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-data
            - The interval of kline see more in: https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info
        Args:
            symbol: the trading pair.
            contract_type: PERPETUAL, CURRENT_MONTH, NEXT_MONTH, CURRENT_QUARTER, NEXT_QUARTER.
            interval: the interval of kline, e.g. 1m, 5m, 1h, 1d, etc.
        Keyword Args:
            limit (Optional[int]): limit the results. async default 500, max 1000.
            start_time (Optional[int]): start time
            end_time (Optional[int]): end time

        """
        return await self._fetch(
            'GET',
            'get_public_continuous_klines',
            "/fapi/v1/continuousKlines",
            pair=symbol,
            contractType=contract_type,
            interval=interval,
            **self._to_api(kwargs)
        )

    async def get_public_index_price_klines(self,
                                            symbol: str,
                                            interval: str,
                                            **kwargs) -> list:
        """**Kline/Candlestick Data for the index price of a pair.**
            Klines are uniquely identified by their open time.

        Notes:
            ``GET /fapi/v1/indexPriceKlines``
        See Also:
            - https://binance-docs.github.io/apidocs/futures/en/#index-price-kline-candlestick-data
            - the interval of kline see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info
        Args:
            symbol: the trading pair.
            interval: the interval of kline, e.g. 1m, 5m, 1h, 1d, etc.
        Keyword Args:
            limit (Optional[int]): limit the results. async default 500, max 1000.
            start_time (Optional[int]): start time
            end_time (Optional[int]): end time
        """
        return await self._fetch(
            'GET',
            'get_public_index_price_klines',
            "/fapi/v1/indexPriceKlines",
            pair=symbol,
            interval=interval,
            **self._to_api(kwargs)
        )

    async def get_public_mark_price_klines(self,
                                           symbol: str,
                                           interval: str,
                                           **kwargs) -> list:
        """**Kline/candlestick bars for the mark price of a symbol.**
            Klines are uniquely identified by their open time.

        Notes:
            ``GET /fapi/v1/markPriceKlines``
        See Also:
            - https://binance-docs.github.io/apidocs/futures/en/#mark-price-kline-candlestick-data
            - the interval of kline see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info
        Args:
            symbol: the trading pair.
            interval: the interval of kline, e.g. 1m, 5m, 1h, 1d, etc.
        Keyword Args:
            limit (Optional[int]): limit the results. async default 500, max 1000.
            start_time (Optional[int]): start time
            end_time (Optional[int]): end time
        """
        return await self._fetch(
            'GET',
            'get_public_mark_price_klines',
            "/fapi/v1/markPriceKlines",
            symbol=symbol,
            interval=interval,
            **self._to_api(kwargs)
        )

    async def get_public_mark_price(self, **kwargs) -> dict | list:
        """**Mark Price and Funding Rate**

        Notes:
            ``GET /fapi/v1/premiumIndex``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#mark-price
        Keyword Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'GET',
            'get_public_mark_price',
            "/fapi/v1/premiumIndex",
            **kwargs
        )

    async def get_public_funding_rate(self,
                                      symbol: str,
                                      **kwargs) -> list:
        """**Funding Rate History**

        Notes:
            ``GET /fapi/v1/fundingRate``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history
        Args:
            symbol: the trading pair.
        Keyword Args:
            limit (Optional[int]): limit the results. async default 500, max 1000.
            start_time (Optional[int]): start time
            end_time (Optional[int]): end time
        Warnings:
            - If start_time and end_time are not sent, the most recent limit datas are returned.
            - If the number of data between start_time and end_time is larger than limit, return as start_time + limit.
            - In ascending order.
        |
        """
        return await self._fetch(
            'GET',
            'get_public_funding_rate',
            "/fapi/v1/fundingRate",
            symbol=symbol,
            **self._to_api(kwargs)
        )

    async def get_public_ticker_24hr_price_change(self, symbol: str) -> dict:
        """**24-hour rolling window price change statistics.**
            Careful when accessing this with no symbol.
            If the symbol is not sent, tickers for all symbols will be returned in an array.
        Notes:
            ``GET /fapi/v1/ticker/24hr``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#24hr-ticker-price-change-statistics
        Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'GET',
            'get_public_ticker_24hr_price_change',
            "/fapi/v1/ticker/24hr",
            symbol=symbol
        )

    async def get_public_ticker_price(self, **kwargs) -> dict | list:
        """**The Latest price for a symbol or symbols.**

        Notes:
            ``GET /fapi/v1/ticker/price``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#symbol-price-ticker
        Keyword Args:
            symbol: the trading symbol.
        **Notes**
            - If the symbol is not sent, prices for all symbols will be returned in an array.
        """
        return await self._fetch(
            'GET',
            'get_public_ticker_price',
            "/fapi/v1/ticker/price",
            **kwargs
        )

    async def get_public_book_ticker(self, **kwargs) -> dict | list:
        """**Best price/qty on the order book for a symbol or symbols.**
        Notes:
            ``GET /fapi/v1/ticker/bookTicker``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#symbol-order-book-ticker
        Keyword Args:
            symbol: the trading symbol.
        **Notes**
            - If the symbol is not sent, prices for all symbols will be returned in an array.
        """
        return await self._fetch(
            'GET',
            'get_public_book_ticker',
            "/fapi/v1/ticker/bookTicker",
            **kwargs
        )

    async def get_public_open_interest(self, symbol: str) -> dict:
        """**Get present open interest of a specific symbol.**

        Notes:
            ``GET /fapi/v1/openInterest``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#open-interest
        Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'GET',
            'get_public_open_interest',
            "/fapi/v1/ticker/bookTicker",
            symbol=symbol
        )

    async def get_public_blvt_kline(self,
                                    symbol: str,
                                    interval: str,
                                    **kwargs) -> list:
        """**Get Historical BLVT NAV Kline**

        Notes:
            ``GET /fapi/v1/lvtKlines``
        See Also:
            - https://binance-docs.github.io/apidocs/futures/en/#historical-blvt-nav-kline-candlestick
            - the period of open interest see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info
        Args:
            symbol: the trading symbol.
            interval: the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d".
        Keyword Args:
            limit (Optional[int]): limit the results. async default 500, max 1000.
            start_time (Optional[int]): start time
            end_time (Optional[int]): end time
        **Notes**
            - If start_time and end_time are not sent, the most recent data is returned.
        """
        return await self._fetch(
            'GET',
            'get_public_blvt_kline',
            "/fapi/v1/lvtKlines",
            symbol=symbol,
            interval=interval,
            **self._to_api(kwargs)
        )

    async def get_public_index_info(self, **kwargs) -> list:
        """**Get Index Composite**

        Notes:
            ``GET /fapi/v1/indexInfo``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information
        Keyword Args:
            symbol: the trading symbol.
        **Notes**
            - Only for composite index symbols.
        """
        return await self._fetch(
            'GET',
            'get_public_index_info',
            "/fapi/v1/indexInfo",
            **kwargs
        )

    async def get_public_asset_index(self, **kwargs) -> dict | list:
        """**Get asset index for Multi-Assets mode**

        Notes:
            ``GET /fapi/v1/assetIndex``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#multi-assets-mode-asset-index
        Keyword Args:
            symbol: Asset pair in multi asset mode (ex: BTCUSD).
        """
        return await self._fetch(
            'GET',
            'get_public_asset_index',
            "/fapi/v1/assetIndex",
            **kwargs)
