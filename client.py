import datetime
import requests
import typing

from requests.auth import HTTPBasicAuth

import exceptions

from settings import MPESA_BASE_URL


class MpesaClient:

    BASE_URL = MPESA_BASE_URL
    ENDPOINTS = {
        'get_token': '/oauth/v1/generate',
    }

    def __init__(self, consumer_key: str,
                 consumer_secret: str,
                 token: str = None,
                 token_expiry: datetime.datetime = None) -> None:

        if not self.BASE_URL:
            raise exceptions.ImproperMpesaSetup('MPESA_BASE_URL env variable has not been set.')

        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret

        if token and token_expiry:
            self._token = token
            self._token_expiry = token_expiry
        else:
            self._get_token()

    def _get_url(self, endpoint_name: str) -> str:
        """
        Compose an endpoint's url.
        :param endpoint_name: name of the endpoint (key in cls.endpoints)
        :return composed_url: the composed url
        """
        if endpoint_name not in self.ENDPOINTS.values():
            raise exceptions.BadMpesaEndpoint

        return f'{self.BASE_URL}{self.ENDPOINTS[endpoint_name]}'

    def _get_token(self) -> None:
        """
        Retrieve the mpesa token, token expiry and set it as an instance variable.
        :return:
        """
        url = self._get_url(endpoint_name='get_token')
        response = requests.get(
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
            response_data = response.json()
            self._token = response_data['access_token']
            # expire token a minute before for sanity
            expires_in_secs = int(response_data['expires_in']) - 60
            self._token_expiry = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in_secs)
        except (KeyError, ValueError, TypeError):
            raise exceptions.BadMpesaResponseData(
                message='Invalid token response data.',
                data=response.text
            )

    @property
    def is_valid_token(self):
        return datetime.datetime.utcnow() < self._token_expiry
