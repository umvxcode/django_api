from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64

class Keamanan:
    def __init__(self):
        self.key = b'ofjndjfndnfjdndn'  # 16-byte key for AES-128
        self.iv = b'euurnsjjjdmdjsxp'  # 16-byte IV for AES

    def enkripsi(self, data: str) -> str:
        # Convert data to bytes
        data = data.encode()
        
        # Pad the data to be multiple of block size (16 bytes for AES)
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        # Create cipher object
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Encrypt data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        # Encode encrypted data in base64 to make it safe for transport
        return base64.b64encode(encrypted_data).decode()

    def dekripsi(self, data: str) -> str:
        # Decode base64 encoded data
        encrypted_data = base64.b64decode(data)

        # Create cipher object
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt data
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Unpad the data
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()

        return data.decode()