from base64 import b64encode

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15


def encrypt_initiator_password(mpesa_certificate_file_location, initiator_password):
    with open(mpesa_certificate_file_location, 'r') as f:
        cert_data = f.read()

    cert = x509.load_pem_x509_certificate(
        data=bytes(cert_data, 'utf-8'),
        backend=default_backend(),
    )
    pub_key = cert.public_key()
    cipher = pub_key.encrypt(bytes(initiator_password, 'utf-8'), PKCS1v15)

    return b64encode(cipher)
