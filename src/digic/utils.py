import json
import requests


def call_api(url):
    """
    Make API request
    :param url: str
    :return: dict
    """

    response = requests.get(url)
    status = response.status_code
    if response.status_code == 200:
        result = response.json()
    else:
        raise Exception('ERROR: {} -- URL: {} -- STATUS: {}'.format(response.text, url, status))

    return result


def read_json(path):
    """
    Read JSON file
    :param path: str
    :return: dict
    """

    with open(path) as f:
        data = json.load(f)

    return data


def write_json(path, data):
    """
    Write JSON file
    :param path: str
    :param data: dict
    :return: None
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def convert_to_eth(wei):
    """
    Convert wei to eth
    :param wei: float, required
    :return: float
    """

    eth = wei / 1000000000000000000

    return eth


def convert_to_btc(satoshi):
    """
    Convert satoshi to btc
    :param satoshi: float, required
    :return: float
    """

    btc = satoshi / 100000000

    return btc
