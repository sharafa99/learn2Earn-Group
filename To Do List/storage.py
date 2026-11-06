import json
from pathlib import Path

def load_storage(file_name):
    storage_path = Path(file_name)
    if storage_path.exists():

        with open(storage_path, "r") as file:
            loaded_data =  json.load(file)
        return {int(k): v for k, v in loaded_data.items()}
    else:
        return {}


def save_task(tasks, file_name ):
        
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)