from pathlib import Path
from digic import utils


digic_path = str(f'{Path.home()}/.digic')


def get_api():
    """
    Get API key
    :return: str
    """

    api_data = utils.read_json(path=f'{digic_path}/api_config.json')

    return api_data['etherscan.io']


def modify_api(vendor, key):
    """
    Modify existing API
    :param vendor: str, required
    :param key: str, required
    :return: None
    """

    file_path = f'{digic_path}/api_config.json'
    api_data = utils.read_json(file_path)
    api_data[vendor] = key
    utils.write_json(file_path, api_data)
