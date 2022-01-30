
class DataStream:

    async def create_private_listen_key(self):
        """**Create a ListenKey (USER_STREAM)**

        Notes:
            ``POST /fapi/v1/listenKey``
        See Also:
             https://binance-docs.github.io/apidocs/futures/en/#start-user-data-stream-user_stream
        """
        return await self._fetch(
            'POST',
            'create_private_listen_key',
            '/fapi/v1/listenKey'
        )

    async def update_private_listen_key(self):
        """**Ping/Keep-alive a ListenKey (USER_STREAM)**

        Notes:
            ``PUT /fapi/v1/listenKey``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#keepalive-user-data-stream-user_stream
        """
        return await self._fetch(
            'PUT',
            'update_private_listen_key',
            '/fapi/v1/listenKey'
        )

    async def delete_private_listen_key(self):
        """**Close a ListenKey (USER_STREAM)**

        Notes:
            ``DELETE /fapi/v1/listenKey``
        See Also:
            https://binance-docs.github.io/apidocs/futures/en/#close-user-data-stream-user_stream
        """
        return await self._fetch(
            'DELETE',
            'delete_private_listen_key',
            '/fapi/v1/listenKey'
        )
