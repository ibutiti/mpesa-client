import datetime
import requests
import typing

from requests.auth import HTTPBasicAuth

import exceptions


class MpesaClient:

    ENDPOINTS: dict[str:str] = {
        'get_token': '/oauth/v1/generate',
        'send_stk_push': '/mpesa/stkpush/v1/processrequest'
    }

    def __init__(self, consumer_key: str,
                 consumer_secret: str,
                 base_url: str,
                 token: str = None,
                 token_expiry: datetime.datetime = None) -> None:

        self._base_url: str = base_url
        self._consumer_key: str = consumer_key
        self._consumer_secret: str = consumer_secret

        if token and token_expiry:
            self._token: str = token
            self._token_expiry: datetime.datetime = token_expiry
        else:
            self._get_token()

    def _get_url(self, endpoint_name: str) -> str:
        """
        Compose an endpoint's url.
        :param endpoint_name: name of the endpoint (key in cls.endpoints)
        :return composed_url: the composed url
        """
        if endpoint_name not in self.ENDPOINTS.keys():
            raise exceptions.BadMpesaEndpoint(endpoint_name=endpoint_name)

        return f'{self._base_url}{self.ENDPOINTS[endpoint_name]}'

    def _get_token(self) -> None:
        """
        Retrieve a valid mpesa token, token expiry and set it as an instance variable.
        :return:
        """
        url: str = self._get_url(endpoint_name='get_token')
        response: requests.Response = requests.get(
            url=url,
            params={
                'grant_type': 'client_credentials'
            },
            auth=HTTPBasicAuth(
                username=self._consumer_key,
                password=self._consumer_secret,
            )

        )

        if response.status_code != 200:
            raise exceptions.BadMpesaResponse(
                status_code=response.status_code,
                response_data=response.text
            )

        try:
            response_data: dict = response.json()
            self._token: str = response_data['access_token']
            # expire token a minute before for sanity
            expires_in_secs: int = int(response_data['expires_in']) - 60
            self._token_expiry: datetime.datetime = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in_secs)
        except (KeyError, ValueError, TypeError):
            raise exceptions.BadMpesaResponseData(
                message='Invalid token response data.',
                data=response.text
            )

    def refresh_token(self) -> None:
        if self.is_valid_token:
            return
        self._get_token()

    @property
    def is_valid_token(self) -> bool:
        return datetime.datetime.utcnow() < self._token_expiry

    def send_stk_push_request(self, business_short_code: int):
        pass
