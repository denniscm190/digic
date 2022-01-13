import os
from digic import utils

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def get_balance(wallet_type, label):
    """
    Get balance of a specific address
    :param wallet_type: str, required
    :param label: str, required
    :return:
    """

    url = 'https://api.etherscan.io/api?module=account&action=balance&address={address:}&tag=latest&apikey={key:}'
    file_path = f'{config_path}/wallet_data.json'
    wallet_data = utils.read_json(file_path)  # {'ethereum': [{'label': 'address'}], 'bitcoin': [{'label': 'address'}]}
