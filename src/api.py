import os
import utils

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def get_api():
    """
    Get API key
    :return: str
    """

    api_data = utils.read_json(path=f'{config_path}/api_data.json')

    return api_data['etherscan.io']


def add_api(vendor, key):
    """
    Add or modify existing API
    :param vendor: str, required
    :param key: str, required
    :return: None
    """

    file_path = f'{config_path}/api_data.json'
    api_data = utils.read_json(file_path)
    api_data[vendor] = key
    utils.write_json(file_path, api_data)
