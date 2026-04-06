from cryptography.fernet import Fernet
import base64, os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_data(data: bytes, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data)
    return salt + encrypted

def decrypt_data(data: bytes, password: str):
    salt = data[:16]
    encrypted = data[16:]
    key = derive_key(password, salt)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted)