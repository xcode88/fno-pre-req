import toml
from typing import Optional, Dict, Any


def load_configurations(file_path) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r') as file:
            config = toml.load(file)
            return config
    except FileNotFoundError as FFE:
        print(f"{FFE.__str__()}")
        return None
    except Exception as E:
        print(f"{E.__str__()}")
        return None


index_FUT = load_configurations(file_path="IDX_FUT.toml")
index_OPT = load_configurations(file_path="IDX_OPT.toml")

print(index_FUT)
print(index_OPT)