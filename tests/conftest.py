import datetime
import pytest

from client import MpesaClient


@pytest.fixture(scope='function')
def mpesa_client():
    return MpesaClient(
        consumer_secret='secret',
        consumer_key='key',
        token='token',
        token_expiry=datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        base_url='https://example.com',
    )
