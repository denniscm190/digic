import os
import click
from pathlib import Path
from digic import utils
from digic import api
from digic import user
from digic import wallet
from digic import portfolio


home_path = str(Path.home())


@click.group(name='cli')
def cli_group():
    """
    A privacy focused command line tool to track your crypto portfolio
    """

    pass


"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
                                            CONFIGURATION COMMANDS                                                                        
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘                   
"""


@click.command()
def init():
    """
    Set up Digic for the first time
    """

    warning = 'This action will delete all your configuration. Do you want to continue?'
    click.confirm(click.style(warning, fg='red'), abort=True)

    # Create files
    digic_path = f'{home_path}/.digic'
    try:
        os.mkdir(digic_path)
    except FileExistsError:
        pass

    user_data = {'username': ''}
    api_data = {'etherscan.io': ''}
    wallet_data = {'ethereum': {}, 'bitcoin': {}}

    utils.write_json(f'{digic_path}/user_config.json', user_data)
    utils.write_json(f'{digic_path}/api_config.json', api_data)
    utils.write_json(f'{digic_path}/wallet_config.json', wallet_data)

    # User
    click.echo('')
    click.echo(click.style('USER CONFIGURATION', bold=True))
    username = click.prompt('Enter a username', default='Satoshi')
    user.modify_username(new_username=username)
    click.echo(f'>>> Hello {username}! Now let\'s set up your wallets')

    # Wallets
    click.echo('')
    click.echo(click.style('WALLET CONFIGURATION', bold=True))
    click.echo('>>> Add the public keys to follow')
    click.echo(click.style('>>> Do not enter your PRIVATE keys. Never!', fg='bright_yellow'))

    confirmation = False
    while True:
        if confirmation:
            if not click.confirm('Do you want to add another wallet?'):
                break

        wallet_type = click.prompt('Select a blockchain', type=click.Choice(['bitcoin', 'ethereum']))
        address = click.prompt('Enter your {} address'.format(wallet_type), type=str)
        label = click.prompt('How do we name your address?', type=str)
        wallet.add_wallet(wallet_type, label, address)
        confirmation = True

    # APIs
    click.echo('')
    click.echo(click.style('API CONFIGURATION', bold=True))
    click.echo('>>> To fetch blockchain data we use the following APIs')
    click.echo('>>> 1) https://etherscan.io')
    click.echo('>>> 2) https://blockchain.com')
    click.echo('>>> 3) https://coingecko.com')
    click.echo('>>> In order to use etherscan.io we need your api key')
    etherscan_key = click.prompt('Enter the etherscan.io key', type=str)
    api.modify_api(vendor='etherscan.io', key=etherscan_key)
    click.echo('>>> Testing APIs...')
    blockchain_url = 'https://blockchain.info/rawblock/00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048'
    coingecko_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin'
    etherscan_url = f'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=1&apikey={etherscan_key}'
    utils.call_api(blockchain_url)
    click.echo(click.style(u'>>> \u2713 blockchain.com', fg='green'))
    utils.call_api(coingecko_url)
    click.echo(click.style(u'>>> \u2713 coingecko.com', fg='green'))
    utils.call_api(etherscan_url)
    click.echo(click.style(u'>>> \u2713 etherscan.io', fg='green'))

    # Reference
    success_message = '>>> Your configuration settings has been saved correctly!'
    help_message = '>>> Enter the --help command if you need guidance using digic'
    reference_message = '>>> Digic is an open source privacy focused command line tool to track your crypto ' \
                        'portfolio.\n>>> Consider contributing to the project https://github.com/denniscm190/digic\n'

    click.echo('')
    click.echo(click.style(success_message, fg='green'))
    click.echo(help_message)
    click.echo(click.style(reference_message, bold=True))


cli_group.add_command(init)


"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
                                                    USER COMMANDS                                                                        
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘                
"""


@click.group(name='user')
def user_group():
    """
    Manage user data
    """

    pass


@click.command(name='list')
def user_list():
    """
    Show username
    """

    username = user.get_username()
    click.echo(f'Username: {username}')


@click.command(name='modify')
@click.option('--username', '-u', type=str, required=True, help='New username')
def user_modify(username):
    """
    Modify username
    """

    user.modify_username(new_username=username)


cli_group.add_command(user_group)
user_group.add_command(user_list)
user_group.add_command(user_modify)


"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
                                                    API COMMANDS                                                                        
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘                   
"""


@click.group(name='api')
def api_group():
    """
    Manage API data
    """

    pass


@click.command(name='list')
def api_list():
    """
    Show API key
    """

    api_key = api.get_api()
    click.echo(f'etherscan.io: {api_key}')


@click.command(name='modify')
@click.option('--key', '-k', type=str, required=True, help='New API key')
def api_modify(key):
    """
    Modify API key
    """

    api.modify_api(vendor='etherscan.io', key=key)


cli_group.add_command(api_group)
api_group.add_command(api_list)
api_group.add_command(api_modify)


"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
                                                    WALLET COMMANDS                                                                        
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘                   
"""


@click.group(name='wallet')
def wallet_group():
    """
    Manage wallet data
    """

    pass


@click.command(name='list')
def wallet_list():
    """
    Show wallets
    """

    wallet_data = wallet.list_wallet()  # {'ethereum': {}, 'bitcoin': {}}
    for wallet_type in list(wallet_data.keys()):  # 'ethereum' , 'bitcoin'
        click.echo(click.style(f'{wallet_type} wallets'.upper(), bold=True))
        wallets = wallet_data[wallet_type]  # {'label': 'address'}
        for label in list(wallets.keys()):
            click.echo(f'{label}: {wallets[label]}')


@click.command(name='add')
@click.option('--type', '-t', 'type_', type=click.Choice(['ethereum', 'bitcoin']), required=True, help='blockchain')
@click.option('--label', '-l', type=str, required=True, help='wallet name')
@click.option('--address', '-a', type=str, required=True, help='address')
def wallet_add(type_, label, address):
    """
    Add wallet
    """

    wallet.add_wallet(type_, label, address)


@click.command(name='remove')
@click.option('--type', '-t', 'type_', type=click.Choice(['ethereum', 'bitcoin']), required=True, help='blockchain')
@click.option('--label', '-l', type=str, required=True, help='wallet name')
def wallet_remove(type_, label):
    """
    Remove wallet
    """

    wallet.remove_wallet(type_, label)


cli_group.add_command(wallet_group)
wallet_group.add_command(wallet_list)
wallet_group.add_command(wallet_add)
wallet_group.add_command(wallet_remove)


"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
                                                PORTFOLIO COMMANDS                                                                        
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘                   
"""


@click.group(name='portfolio')
def portfolio_group():
    """
    Portfolio statistics
    """

    pass


@click.command(name='balance')
@click.option('--type', '-t', 'type_', type=click.Choice(['ethereum', 'bitcoin']), required=True, help='blockchain')
@click.option('--label', '-l', type=str, required=True, help='wallet name')
def portfolio_balance(type_, label):
    """
    Show portfolio balance
    """

    balance = portfolio.get_balance(type_, label)
    click.echo(click.style(f'{type_} wallet'.upper(), bold=True))
    click.echo(f'{label}: {balance[label]}')


@click.command(name='txs')
def portfolio_transactions():
    """
    Show the latest transactions of a specific address
    """

    pass


cli_group.add_command(portfolio_group)
portfolio_group.add_command(portfolio_balance)


if __name__ == '__main__':
    cli_group()
