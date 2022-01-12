import os
from digic import utils

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def list_wallet():
    """
    Get wallets
    :return: dict
    """

    wallet_data = utils.read_json(f'{config_path}/wallet_data.json')

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
    wallet_data = utils.read_json(file_path)
    wallets = wallet_data[wallet_type]
    new_address = {label: address}
    wallets.append(new_address)
    wallet_data[wallet_type] = wallets
    utils.write_json(file_path, wallet_data)


def remove_wallet(wallet_type, label):
    """
    Remove wallet
    :param wallet_type: str, required
    :param label: str, required
    :return: None
    """

    file_path = f'{config_path}/wallet_data.json'
    wallet_data = utils.read_json(file_path)  # {'ethereum': [{'label': 'address'}], 'bitcoin': [{'label': 'address'}]}
    wallets = wallet_data[wallet_type]  # [{'label': 'address'}]
    for wallet_item in wallets:  # {'label': 'address'}
        for key in list(wallet_item.keys()):  # 'label'
            if key == label:
                wallets.remove(wallet_item)

    wallet_data[wallet_type] = wallets
    utils.write_json(file_path, wallet_data)
