import json
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def init_api(api_vendor, key):
    with open('{}/api_data.json'.format(config_path), 'w') as api_file:
        api = {api_vendor: key}
        json.dump(api, api_file)


def add_api(api_vendor, key):
    with open('{}/api_data.json'.format(config_path)) as api_file:
        api_dict = json.load(api_file)

    with open('{}/api_data.json'.format(config_path), 'w') as api_file:
        api_dict[api_vendor] = key
        json.dump(api_dict, api_file)
