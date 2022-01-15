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


def get_balance_wallet(wallet_type, label):
    """
    Get balance of a specific address
    :param wallet_type: str, required
    :param label: str, required
    :return: dict
    """

    wallet_file_path = f'{digic_path}/wallet_config.json'
    api_file_path = f'{digic_path}/api_config.json'
    wallet_data = utils.read_json(wallet_file_path)  # {'ethereum': {}, 'bitcoin': {}}
    wallets = wallet_data[wallet_type]
    address = wallets[label]

    if wallet_type == 'ethereum':
        key = utils.read_json(api_file_path)['etherscan.io']
        url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={key}'
        response = utils.call_api(url)
        eth_balance = utils.convert_to_eth(float(response['result']))
        eth_balance = round(eth_balance, 5)
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
        response = utils.call_api(url)
        usd_price = response['ethereum']['usd']
        usd_balance = round(usd_price * eth_balance, 2)
        result = {label: f'{eth_balance:,} ETH ({usd_balance:,} USD)'}
    else:
        url = f'https://blockchain.info/rawaddr/{address}'
        response = utils.call_api(url)
        btc_balance = utils.convert_to_btc(response['final_balance'])
        btc_balance = round(btc_balance, 5)
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
        response = utils.call_api(url)
        usd_price = response['bitcoin']['usd']
        usd_balance = round(usd_price * btc_balance, 2)
        result = {label: f'{btc_balance:,} BTC ({usd_balance:,} USD)'}

    return result
