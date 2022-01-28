import sys

async def new_listen_key(self):
    """
    |
    | **Create a ListenKey (USER_STREAM)**
    :API endpoint: ``POST /fapi/v1/listenKey``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#start-user-data-stream-user_stream
    |
    """

    url_path = "/fapi/v1/listenKey"
    return await self._fetch(True, 'POST', sys._getframe().f_code.co_name, url_path)


async def update_listen_key(self):
    """
    |
    | **Ping/Keep-alive a ListenKey (USER_STREAM)**
    :API endpoint: ``PUT /fapi/v1/listenKey``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#keepalive-user-data-stream-user_stream
    :parameter listenKey: string
    |
    """
    url_path = "/fapi/v1/listenKey"
    return await self._fetch(True, 'PUT', sys._getframe().f_code.co_name, url_path)


async def close_listen_key(self):
    """
    |
    | **Close a ListenKey (USER_STREAM)**
    :API endpoint: ``DELETE /fapi/v1/listenKey``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#close-user-data-stream-user_stream
    :parameter listenKey: string
    |
    """
    url_path = "/fapi/v1/listenKey"
    return await self._fetch(True, 'DELETE', sys._getframe().f_code.co_name, url_path)
