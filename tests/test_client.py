import datetime

import pytest

import exceptions

from client import MpesaClient


class TestMpesaClientSetup:

    @pytest.mark.parametrize(
        'input_value, expected, exception', [
            ('get_token', MpesaClient.ENDPOINTS['get_token'], None),
            ('invalid', None, exceptions.BadMpesaEndpoint)
        ]
    )
    def test_get_url_function(self, input_value, expected, exception, mpesa_client):
        if exception:
            with pytest.raises(exception):
                mpesa_client._get_url(input_value)
        else:
            assert f'{mpesa_client._base_url}{expected}' == mpesa_client._get_url(input_value)

    def test_get_token_function(self):
        pass

    def test_is_valid_token_property(self):
        pass
