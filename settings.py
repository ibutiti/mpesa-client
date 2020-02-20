import os

from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY: str = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET: str = os.environ.get('CONSUMER_SECRET')
MPESA_BASE_URL: str = os.environ.get('MPESA_BASE_URL')
INITIATOR_PASSWORD: str = os.environ.get('INITIATOR_PASSWORD')
MPESA_CERTIFICATE_FILE_PATH: str = os.environ.get('MPESA_CERTIFICATE_FILE_PATH')
