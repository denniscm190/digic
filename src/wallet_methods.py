import json
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def init_wallet(wallet_type, label, address):
    with open('{}/wallet_data.json'.format(config_path), 'w') as wallet_file:
        wallet_data = {wallet_type: [{label: address}]}
        json.dump(wallet_data, wallet_file)


def get_wallet_data():
    with open('{}/wallet_data.json'.format(config_path)) as wallet_file:
        wallet_data = json.load(wallet_file)

    return wallet_data


def add_wallet(wallet_type, label, address):
    with open('{}/wallet_data.json'.format(config_path)) as wallet_file:
        wallet_data = json.load(wallet_file)

    with open('{}/wallet_data.json'.format(config_path), 'w') as wallet_file:
        try:
            wallets = wallet_data[wallet_type]
        except KeyError:
            wallets = []

        new_wallet = {label: address}
        wallets.append(new_wallet)
        wallet_data[wallet_type] = wallets
        json.dump(wallet_data, wallet_file)
