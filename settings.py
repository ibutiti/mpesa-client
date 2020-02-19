import os

from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
MPESA_BASE_URL = os.environ.get('MPESA_BASE_URL')
INITIATOR_PASSWORD = os.environ.get('INITIATOR_PASSWORD')
MPESA_CERTIFICATE_FILE_PATH = os.environ.get('MPESA_CERTIFICATE_FILE_PATH')
