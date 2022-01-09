import os
import utils

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


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
