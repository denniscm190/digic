import os
import utils

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


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
