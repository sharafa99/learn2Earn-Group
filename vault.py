import json
from pathlib import Path

def load_vault(file_name):
    vault_path = Path(file_name)
    if vault_path.exists():

        with open(vault_path, "r") as file:
            return json.load(file)
    else:
        return []

def save_vault(vault, file_name):
    with open(file_name, "w") as file:
        json.dump(vault, file)
