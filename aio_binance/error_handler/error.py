

class BinanceException(Exception):

    def __init__(
            self,
            error_code,
            error_message):
        self.code = error_code
        self.msg = error_message
