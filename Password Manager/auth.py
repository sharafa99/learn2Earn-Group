import secrets
import json
import hashlib
from pathlib import Path
def create_auth(password):
    password_byte = password.encode()
    salt = secrets.token_bytes(16)

    hashed_password = hashlib.pbkdf2_hmac(
        "sha256",
        password_byte,
        salt,
        600_000
    )

    salt_hex = salt.hex()
    hashed_password_hex = hashed_password.hex()
    auth_data = {}
    auth_data["salt"] = salt_hex
    auth_data["password_hash"] = hashed_password_hex
    return auth_data

def load_auth(file_name):
    auth_path = Path(file_name)
    if auth_path.exists():

        with open(auth_path, "r") as file:
            return json.load(file)
    else:
        return {}

def save_auth(auth_data, file_name):
    with open(file_name, "w") as file:
        json.dump(auth_data, file)
