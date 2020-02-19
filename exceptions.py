class ImproperMpesaSetup(Exception):
    pass


class BadMpesaEndpoint(Exception):
    def __init__(self, endpoint_name: str):
        self.endpoint_name = endpoint_name

    def __str__(self):
        return f'Endpoint \'{self.endpoint_name}\' does not exist'


class BadMpesaResponse(Exception):
    def __init__(self, status_code: int, response_data: str, message: str) -> None:
        self.status_code = status_code
        self.response_data = response_data
        self.message = message

    def __str__(self):
        return f'{self.message} Status Code: {self.status_code}. Response data: {self.response_data}'


class BadMpesaResponseData(Exception):
    def __init__(self, data: str, message: str):
        self.data = data
        self.message = message

    def __str__(self):
        return f'{self.message}. Response data: {self.data}'
