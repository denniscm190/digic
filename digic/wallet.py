from pathlib import Path
from digic import utils


digic_path = str(f'{Path.home()}/.digic')


def list_wallet():
    """
    Get wallets
    :return: dict
    """

    wallet_data = utils.read_json(f'{digic_path}/wallet_config.json')  # {'ethereum': {}, 'bitcoin': {}}

    return wallet_data


def add_wallet(wallet_type, label, address):
    """
    Add wallet
    :param wallet_type: str, required
    :param label: str, required
    :param address: str, required
    :return: None
    """

    file_path = f'{digic_path}/wallet_config.json'
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

    file_path = f'{digic_path}/wallet_config.json'
    wallet_data = utils.read_json(file_path)  # # {'ethereum': {}, 'bitcoin': {}}
    wallets = wallet_data[wallet_type]  # {'label': 'address'}
    del wallets[label]
    utils.write_json(file_path, wallet_data)
