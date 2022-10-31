import ujson


class Account:

    async def change_private_position_mode(self, dual_side_position: str) -> dict:
        """**Change Position Mode (TRADE)**
            Change user's position mode (Hedge Mode or One-way Mode) on EVERY symbol
        Notes:
            ``POST /fapi/v1/positionSide/dual``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#change-position-mode-trade
        Args:
            dual_side_position: "true": Hedge Mode; "false": One-way Mode
        """
        return await self._fetch(
            'POST',
            'change_private_position_mode',
            '/fapi/v1/positionSide/dual',
            dualSidePosition=dual_side_position
        )

    async def get_private_position_mode(self) -> dict:
        """**Get Current Position Mode (USER_DATA)**
            Get user's position mode (Hedge Mode or One-way Mode) on EVERY symbol

        Notes:
            ``GET /fapi/v1/positionSide/dual``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#get-current-position-mode-user_data
        """
        return await self._fetch(
            'GET',
            'get_private_position_mode',
            '/fapi/v1/positionSide/dual'
        )

    async def change_private_multi_asset_mode(self, multi_assets_margin: str) -> dict:
        """**Change Multi-Assets Mode (TRADE)**
            Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

        Notes:
            ``POST /fapi/v1/multiAssetsMargin``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#change-multi-assets-mode-trade
        Args:
            multi_assets_margin: "true": Multi-Assets Mode; "false": Single-Asset Mode
        """
        return await self._fetch(
            'POST',
            'change_private_multi_asset_mode',
            '/fapi/v1/multiAssetsMargin',
            multiAssetsMargin=multi_assets_margin
        )

    async def get_private_multi_asset_mode(self) -> dict:
        """**Get Current Multi-Assets Mode (USER_DATA)**
            Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol

        Notes:
            ``GET /fapi/v1/multiAssetsMargin``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#get-current-multi-assets-mode-user_data
        """
        return await self._fetch(
            'GET',
            'get_private_multi_asset_mode',
            '/fapi/v1/multiAssetsMargin'
        )

    async def create_private_order(self,
                                   symbol: str,
                                   side: str,
                                   type_order: str,
                                   **kwargs) -> dict:
        """**New Order (TRADE)**
            Send a new order

        Notes:
            ``POST /fapi/v1/order``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#new-order-trade
        Args:
            symbol: the trading symbol.
            side: Order direction BUY or SELL
            type_order: type order e.n. LIMIT, MARKET, STOP/TAKE_PROFIT,
                        STOP_MARKET/TAKE_PROFIT_MARKET, TRAILING_STOP_MARKET
        Keyword Args:
            position_side: (str) default BOTH for One-way Mode; LONG or SHORT for Hedge Mode.
                                It must be passed in Hedge Mode.
            time_in_force: (str) Order with type STOP, parameter timeInForce can be sent ( default GTC).
            quantity: (str) Cannot be sent with close_position=true(Close-All)
            reduce_only: (str) "true" or "false". default "false". Cannot be sent in Hedge Mode;
                            cannot be sent with closePosition=true
            price: (str)
            new_client_order_id: (str) An unique ID among open orders. Automatically generated if not sent.
            stop_price: (str) Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
            close_position: (str) true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
            activation_price: (str) Use with TRAILING_STOP_MARKET orders,
                                default is the latest price (supporting different workingType).
            callback_rate: (str) Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
            working_type: (str) stop_price triggered by: "MARK_PRICE", "CONTRACT_PRICE". default "CONTRACT_PRICE".
            price_protect: (str) "TRUE" or "FALSE", async default "FALSE".
                            Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
            new_order_resp_type: (str) "ACK" or "RESULT", async default "ACK".
        """
        return await self._fetch(
            'POST',
            'create_private_order',
            '/fapi/v1/order',
            symbol=symbol,
            side=side,
            type=type_order,
            **self._to_api(kwargs)
        )

    async def create_private_order_test(self,
                                        symbol: str,
                                        side: str,
                                        type_order: str,
                                        **kwargs) -> dict:
        """**New Test Order (TRADE)**
            Send a new test order
        Notes:
            ``POST /fapi/v1/order/test``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#new-order-trade
        Args:
            symbol: the trading symbol.
            side: Order direction BUY or SELL
            type_order: type order e.n. LIMIT, MARKET, STOP/TAKE_PROFIT,
                        STOP_MARKET/TAKE_PROFIT_MARKET, TRAILING_STOP_MARKET
        Keyword Args:
            position_side: (str) default BOTH for One-way Mode; LONG or SHORT for Hedge Mode.
                                It must be passed in Hedge Mode.
            time_in_force: (str) Order with type STOP, parameter timeInForce can be sent ( default GTC).
            quantity: (str) Cannot be sent with close_position=true(Close-All)
            reduce_only: (str) "true" or "false". default "false". Cannot be sent in Hedge Mode;
                            cannot be sent with closePosition=true
            price: (str)
            new_client_order_id: (str) An unique ID among open orders. Automatically generated if not sent.
            stop_price: (str) Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
            close_position: (str) true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
            activation_price: (str) Use with TRAILING_STOP_MARKET orders,
                                default is the latest price (supporting different workingType).
            callback_rate: (str) Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
            working_type: (str) stop_price triggered by: "MARK_PRICE", "CONTRACT_PRICE". default "CONTRACT_PRICE".
            price_protect: (str) "TRUE" or "FALSE", async default "FALSE".
                            Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
            new_order_resp_type: (str) "ACK" or "RESULT", async default "ACK".
        """
        return await self._fetch(
            'POST',
            'create_private_order_test',
            '/fapi/v1/order/test',
            symbol=symbol,
            side=side,
            type=type_order,
            **self._to_api(kwargs)
        )

    async def create_private_batch_order(self, batch_orders: list[dict]) -> dict:
        """**Place Multiple Orders (TRADE)**
            Post a new batch order*
        Notes:
            ``POST /fapi/v1/batchOrders``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade
        batch_orders:
            symbol (str):
                the trading symbol.
            side (str):
                Order direction BUY or SELL
            type (str):
                type order e.n. LIMIT, MARKET, STOP/TAKE_PROFIT, STOP_MARKET/TAKE_PROFIT_MARKET, TRAILING_STOP_MARKET
            position_side (str):
                default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be passed in Hedge Mode.
            time_in_force (str):
                Order with type STOP, parameter timeInForce can be sent ( default GTC).
            quantity (str):
                Cannot be sent with close_position=true(Close-All)
            reduce_only (str):
                "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
            price (str):

            new_client_order_id (str):
                An unique ID among open orders. Automatically generated if not sent.
            stop_price (str):
                Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
            close_position (str):
                true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
            activation_price (str):
                Use with TRAILING_STOP_MARKET orders, default is the latest price (supporting different workingType).
            callback_rate (str):
                Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
            working_type (str):
                stop_price triggered by: "MARK_PRICE", "CONTRACT_PRICE". default "CONTRACT_PRICE".
            price_protect (str):
                "true" or "false", default "false". Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
            new_order_resp_type (str):
                "ACK" or "RESULT", async default "ACK".
        Notes:
            Batch orders are processed concurrently, and the order of matching is not guaranteed.

            The order of returned contents for batch orders is the same as the order of the order list.

            batchOrders (list): order list. Max 5 orders

            batchOrders is the list of order parameters in JSON

        Examples:
            batch_orders = [
                {
                    "symbol":"BTCUSDT",

                    "side": "SELL",

                    "type": "LIMIT",

                    "quantity": "0.001",

                    "time_in_force": "GTC",

                    "reduce_only": "false",

                    "price": "9563.51"
                },

                {
                    "symbol":"BTCUSDT",

                    "side": "SELL",

                    "type": "LIMIT",

                    "quantity": "0.001",

                    "time_in_force": "GTC",

                    "reduce_only": "false",

                    "price": "9613.51"
                }
            ]
        """
        return await self._fetch(
            'POST',
            'create_private_batch_order',
            '/fapi/v1/batchOrders',
            batchOrders=ujson.dumps(self._to_api(batch_orders))
        )

    async def get_private_order(self,
                                symbol: str,
                                order_id: int | str) -> dict:
        """**Query Order (USER_DATA)**
            Check an order's status
        Notes:
            ``GET /fapi/v1/order``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#query-order-user_data
        Args:
            symbol: the trading symbol.
            order_id: int order_id or string orig_client_order_id
        """
        params = {"symbol": symbol, "orderId": order_id}\
            if isinstance(order_id, int)\
            else {"symbol": symbol, "origClientOrderId": order_id}
        return await self._fetch(
            'GET',
            'get_private_order',
            '/fapi/v1/order',
            **params
        )

    async def delete_private_order(self,
                                   symbol: str,
                                   order_id: int | str) -> dict:
        """**Cancel Order (TRADE)**
            Cancel an active order.
        Notes:
            ``DELETE /fapi/v1/order``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#cancel-order-trade
        Args:
            symbol: the trading symbol.
            order_id: int order_id or string orig_client_order_id
        |
        """
        params = {"symbol": symbol, "orderId": order_id}\
            if isinstance(order_id, int)\
            else {"symbol": symbol, "origClientOrderId": order_id}
        return await self._fetch(
            'DELETE',
            'delete_private_order',
            '/fapi/v1/order',
            **params
        )

    async def delete_private_all_open_orders(self, symbol: str) -> dict:
        """**Cancel All Open Orders (TRADE)**

        Notes:
            ``DELETE /fapi/v1/allOpenOrders``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#cancel-all-open-orders-trade
        Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'DELETE',
            'delete_private_all_open_orders',
            '/fapi/v1/allOpenOrders',
            symbol=symbol
        )

    async def delete_private_batch_order(self,
                                         symbol: str,
                                         order_id_list: list[int | str]) -> dict:
        """**Cancel Multiple Orders (TRADE)**
            Cancel a new batch order*
        Notes:
            ``DELETE /fapi/v1/batchOrders``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#cancel-multiple-orders-trade
        Args:
            symbol: the trading symbol.
            order_id_list: int list; max length 10 e.g. [1234567, 2345678] or string list; max length 10 e.g.
                                    ["my_id_1", "my_id_2"], encode the double quotes. No space after comma.
        """
        params = {"symbol": symbol, "orderIdList": ujson.dumps(order_id_list)}\
            if isinstance(order_id_list[0], int)\
            else {"symbol": symbol, "origClientOrderIdList": ujson.dumps(order_id_list)}
        return await self._fetch(
            'DELETE',
            'delete_private_batch_order',
            '/fapi/v1/batchOrders',
            **params
        )

    async def delete_private_order_countdown(self,
                                             symbol: str,
                                             count_down_time: int) -> dict:
        """**Auto-Cancel All Open Orders (TRADE)**
            Cancel all open orders of the specified symbol at the end of the specified countdown.*
        Notes:
            ``POST /fapi/v1/countdownCancelAll``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#auto-cancel-all-open-orders-trade
        Args:
            symbol: the trading symbol.
            count_down_time: countdown time, 1000 for 1 second. 0 to cancel the timer.
        Notes:
            The endpoint should be called repeatedly as heartbeats so that the existing
            countdown time can be canceled and replaced by a new one.
        Examples:
            Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).

            If this endpoint is not called within 120 seconds,
            all your orders of the specified symbol will be automatically canceled.

            If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.
        Notes:
            The system will check all countdowns approximately every 10 milliseconds,
            so please note that sufficient redundancy should be considered when using this function.

            We do not recommend setting the countdown time to be too precise or too small.
        """
        return await self._fetch(
            'POST',
            'delete_private_order_countdown',
            '/fapi/v1/countdownCancelAll',
            symbol=symbol,
            countdownTime=count_down_time
        )

    async def get_private_open_order(self,
                                     symbol: str,
                                     order_id: int | str) -> dict:
        """**Query Current Open Order (USER_DATA)**
            Get all open orders on a symbol.*
        Notes:
            ``GET /fapi/v1/openOrder``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#query-current-open-order-user_data
        Args:
            symbol: the trading symbol.
            order_id: int order_id or string orig_client_order_id
        Notes:
            If the queried order has been filled or cancelled,
            the error message "Order does not exist" will be returned.
        """
        params = {"symbol": symbol, "orderId": order_id}\
            if isinstance(order_id, int)\
            else {"symbol": symbol, "origClientOrderId": order_id}
        return await self._fetch(
            'GET',
            'get_private_open_order',
            '/fapi/v1/openOrder',
            **params
        )

    async def get_private_all_open_orders(self, **kwargs) -> dict:
        """**Current All Open Orders (USER_DATA)**
            Get all open orders on a symbol. Careful when accessing this with no symbol.

            If the symbol is not sent, orders for all symbols will be returned in an array.
        Notes:
            ``GET /fapi/v1/openOrders``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#current-all-open-orders-user_data
        Keyword Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'GET',
            'get_private_all_orders',
            '/fapi/v1/openOrders',
            **kwargs
        )

    async def get_private_all_orders(self,
                                     symbol: str,
                                     **kwargs) -> dict:
        """**All Orders (USER_DATA)**
            Get all account orders; active, canceled, or filled.
        Notes:
            ``GET /fapi/v1/allOrders``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#all-orders-user_data
        Args:
            symbol: the trading symbol.
        Keyword Args:
            order_id: (optional int) If orderId is set, it will get orders >= that orderId.
            Otherwise, most recent orders are returned.
            start_time: (optional int) The query time period must be less than 7 days( default as the recent 7 days).
            end_time: (optional int)
            limit: (optional int) Default 500; max 1000.
        """
        return await self._fetch(
            'GET',
            'get_private_all_orders',
            '/fapi/v1/allOrders',
            symbol=symbol,
            **self._to_api(kwargs)
        )

    async def get_private_balance(self) -> dict:
        """**Futures Account Balance V2 (USER_DATA)**
            Get current account balance
        Notes:
            ``GET /fapi/v2/balance``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#futures-account-balance-v2-user_data
        """
        return await self._fetch(
            'GET',
            'get_private_balance',
            '/fapi/v2/balance'
        )

    async def get_private_account_info(self) -> dict:
        """**Account Information V2 (USER_DATA)**
            Get current account information
        Notes:
            ``GET /fapi/v2/account``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#account-information-v2-user_data
        """
        return await self._fetch(
            'GET',
            'get_private_account_info',
            '/fapi/v2/account'
        )

    async def change_private_leverage(self,
                                      symbol: str,
                                      leverage: int) -> dict:
        """**Change Initial Leverage (TRADE)**
            Change user's initial leverage of specific symbol market.*
        Notes:
            ``POST /fapi/v1/leverage``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#change-initial-leverage-trade
        Args:
            symbol: the trading symbol.
            leverage: target initial leverage: int from 1 to 125.
        """
        return await self._fetch(
            'POST',
            'change_private_leverage',
            '/fapi/v1/leverage',
            symbol=symbol,
            leverage=leverage
        )

    async def change_private_margin_type(self,
                                         symbol: str,
                                         margin_type: str) -> dict:
        """**Change margin type (TRADE)**
            Change user's margin type of specific symbol market.
        Notes:
            ``POST /fapi/v1/marginType``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#change-margin-type-trade
        Args:
            symbol: the trading symbol.
            margin_type: ISOLATED, CROSSED.
        """
        return await self._fetch(
            'POST',
            'change_private_margin_type',
            '/fapi/v1/marginType',
            symbol=symbol,
            marginType=margin_type
        )

    async def change_private_isolated_position_margin(self,
                                                      symbol: str,
                                                      amount: str,
                                                      type_position: int,
                                                      **kwargs) -> dict:
        """**Modify Isolated Position Margin (TRADE)**

        Notes:
            ``POST /fapi/v1/positionMargin``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#modify-isolated-position-margin-trade
        Args:
            symbol: the trading symbol.
            amount: str
            type_position: 1: Add position margin, 2: Reduce position margin
        Keyword Args:
            position_side: (optional str) default BOTH for One-way Mode,
                LONG or SHORT for Hedge Mode. It must be sent with Hedge Mode.
        """
        return await self._fetch(
            'POST',
            'change_private_isolated_position_margin',
            '/fapi/v1/positionMargin',
            symbol=symbol,
            amount=amount,
            type=type_position,
            **self._to_api(kwargs)
        )

    async def get_private_position_margin_history(self,
                                                  symbol: str,
                                                  **kwargs) -> dict:
        """**Get Position Margin Change History (TRADE)**
            Get position margin history on a symbol.*
        Notes:
            ``GET /fapi/v1/positionMargin/history``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#get-position-margin-change-history-trade
        Args:
            symbol: the trading symbol.
        Keyword Args:
            type: (optional int) 1: Add position margin, 2: Reduce position margin.
            start_time: (optional int)
            end_time: (optional int)
            limit: (optional int) default: 500.
        """
        return await self._fetch(
            'GET',
            'get_private_position_margin_history',
            '/fapi/v1/positionMargin/history',
            symbol=symbol,
            **self._to_api(**kwargs)
        )

    async def get_private_position_risk(self, symbol: str) -> dict:
        """**Position Information V2 (USER_DATA)**
            Get current position information.
        Notes:
            ``GET /fapi/v2/positionRisk``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#position-information-v2-user_data
        Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'GET',
            'get_private_position_risk',
            '/fapi/v2/positionRisk',
            symbol=symbol
        )

    async def get_private_account_trades(self,
                                         symbol: str,
                                         **kwargs) -> dict:
        """**Account Trade List (USER_DATA)**
            *Get trades for a specific account and symbol.*
        Notes:
            ``GET /fapi/v1/userTrades``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#account-trade-list-user_data
        Args:
            symbol: the trading symbol.
        Keyword Args:
            start_time: (optional int)
            end_time: (optional int)
            from_id: (optional int) trade ID to fetch from, default gets most recent trades.
            limit: (optional int) default: 500, max: 1000.
        Notes:
            If startTime and endTime are both not sent, then the last 7 days' data will be returned.

            The time between startTime and endTime cannot be longer than 7 days.

            The parameter fromId cannot be sent with startTime or endTime.
        """
        return await self._fetch(
            'GET',
            'get_private_account_trades',
            '/fapi/v1/userTrades',
            symbol=symbol,
            **self._to_api(kwargs)
        )

    async def get_private_income_history(self, **kwargs) -> dict:
        """**Get Income History (USER_DATA)**
            Get trades for a specific account and symbol.
        Notes:
            ``GET /fapi/v1/income``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#get-income-history-user_data
        Keyword Args:
            symbol: the trading symbol.
            income_type: (optional str)
                "TRANSFER", "WELCOME_BONUS", "REALIZED_PNL", "FUNDING_FEE", "COMMISSION" "INSURANCE_CLEAR".
            start_time: (optional int) timestamp in ms to get funding from INCLUSIVE.
            end_time: (optional int) timestamp in ms to get funding from INCLUSIVE.
            limit: (optional int) default: 100, max: 1000.
        Notes:
            If neither startTime nor endTime is sent, the recent 7-day data will be returned.

            If incomeType is not sent, all kinds of flow will be returned

            "trandId" is unique in the same income_type for a user
        """
        return await self._fetch(
            'GET',
            'get_private_income_history',
            '/fapi/v1/income',
            **self._to_api(kwargs)
        )

    async def get_private_leverage_brackets(self, **kwargs) -> dict:
        """**Notional and Leverage Brackets (USER_DATA)**
            Get notional and leverage bracket.*
        Notes:
            ``GET /fapi/v1/leverageBracket``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#notional-and-leverage-brackets-user_data
        Keyword Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'GET',
            'get_private_leverage_brackets',
            '/fapi/v1/leverageBracket',
            **kwargs
        )

    async def get_private_adl_quantile(self, **kwargs) -> dict:
        """**Position ADL Quantile Estimation (USER_DATA)**
            Get Position ADL Quantile Estimation
        Notes:
            ``GET /fapi/v1/adlQuantile``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#position-adl-quantile-estimation-user_data
        Keyword Args:
            symbol: the trading symbol.
        Notes:
            Values update every 30s.

            Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.

            For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode,
            "LONG", "SHORT", and "BOTH" will be returned to show the positions'
            adl quantiles of different position sides.

            If the positions of the symbol are crossed margined in Hedge Mode:
                - "HEDGE" as a sign will be returned instead of "BOTH"
            A same value calculated on unrealized pnls on long and short sides'
            positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
        """
        return await self._fetch(
            'GET',
            'get_private_adl_quantile',
            '/fapi/v1/adlQuantile',
            **kwargs
        )

    async def get_private_force_orders(self, **kwargs) -> dict:
        """**User's Force Orders (USER_DATA)**
            Get User's Force Orders
        Notes:
            ``GET /fapi/v1/forceOrders``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#user-39-s-force-orders-user_data
        Keyword Args:
            symbol: the trading symbol.
            auto_close_type: (optional str) "LIQUIDATION" for liquidation orders, "ADL" for ADL orders.
                If "auto_close_type" is not sent, orders with both of the types will be returned
            start_time: (optional int) If "start_time" is not sent, data within 7 days before "end_time" can be queried
            end_time: (optional int)
            Limit: (optional int) default 50, max 100.
        """
        return await self._fetch(
            'GET',
            'get_private_force_orders',
            '/fapi/v1/forceOrders',
            **self._to_api(kwargs)
        )

    async def get_private_api_trading_status(self, **kwargs) -> dict:
        """**User API Trading Quantitative Rules Indicators (USER_DATA)**
            Get User API Trading Quantitative Rules Indicators
        Notes:
            ``GET /fapi/v1/apiTradingStatus``
        See Also:
            API doc: https://binance-docs.github.io/apidocs/futures/en/#user-api-trading-quantitative-rules-indicators-user_data

            For more information on this, please refer to the: https://www.binance.com/en/support/faq/4f462ebe6ff445d4a170be7d9e897272
        Keyword Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'GET',
            'get_private_api_trading_status',
            '/fapi/v1/apiTradingStatus',
            **kwargs
        )

    async def get_private_commission_rate(self, symbol: str) -> dict:
        """**User Commission Rate (USER_DATA)**
            Get commission rate of symbol
        Notes:
            ``GET /fapi/v1/commissionRate``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#user-commission-rate-user_data
        Args:
            symbol: the trading symbol.
        """
        return await self._fetch(
            'GET',
            'get_private_commission_rate',
            '/fapi/v1/commissionRate',
            symbol=symbol
        )

