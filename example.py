import toml
from typing import Optional, Dict, Any
from urllib import request


def download_file_as(file_url: str, save_as_name: str):
    try:
        response = request.urlretrieve(file_url, save_as_name)
        print(response)
    except Exception as E:
        print(E)


download_file_as("https://xcode88.github.io/fno-pre-req/IDX_FUT.toml", "IDX_FUT.toml")
download_file_as("https://xcode88.github.io/fno-pre-req/IDX_OPT.toml", "IDX_OPT.toml")


def load_configurations(file_path) -> Optional[Dict[str, Any]]:
    """ Load Configurations from downloaded toml """
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
