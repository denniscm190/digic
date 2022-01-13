import os
from digic import utils

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def list_wallet():
    """
    Get wallets
    :return: dict
    """

    wallet_data = utils.read_json(f'{config_path}/wallet_data.json')  # {'ethereum': {}, 'bitcoin': {}}

    return wallet_data


def add_wallet(wallet_type, label, address):
    """
    Add wallet
    :param wallet_type: str, required
    :param label: str, required
    :param address: str, required
    :return: None
    """

    file_path = f'{config_path}/wallet_data.json'
    wallet_data = utils.read_json(file_path)  # {'ethereum': {}, 'bitcoin': {}}
    wallets = wallet_data[wallet_type]  # {'label': 'address'}
    wallets[label] = address  # Add new wallet
    utils.write_json(file_path, wallet_data)


def remove_wallet(wallet_type, label):
    """
    Remove wallet
    :param wallet_type: str, required
    :param label: str, required
    :return: None
    """

    file_path = f'{config_path}/wallet_data.json'
    wallet_data = utils.read_json(file_path)  # # {'ethereum': {}, 'bitcoin': {}}
    wallets = wallet_data[wallet_type]  # {'label': 'address'}
    del wallets[label]
    utils.write_json(file_path, wallet_data)
