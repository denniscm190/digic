import os

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def get_balance():
    """
    Get balance for each address and compute the total of the portfolio
    :return:
    """

    url = 'https://api.etherscan.io/api?module=account&action=balancemulti&address={addresses:}' \
          '&tag=latest&apikey={key:}'

    file_path = f'{config_path}/wallet_data.json'
