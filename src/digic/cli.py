import os
import click
from digic import api, utils, wallet, user


home_path = os.path.expanduser('~')


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
    set up Digic
    """

    # Create files
    digic_path = os.path.join(home_path, '.digic')
    try:
        os.mkdir(digic_path)
    except FileExistsError:
        warning = 'This action will delete all your configuration settings. Do you want to continue?'
        click.confirm(click.style(warning, fg='red'), abort=True)

    user_data = {'username': ''}
    api_data = {'etherscan.io': ''}
    wallet_data = {'ethereum': {}, 'bitcoin': {}}

    utils.write_json(os.path.join(digic_path, 'user_config.json'), user_data)
    utils.write_json(os.path.join(digic_path, 'api_config.json'), api_data)
    utils.write_json(os.path.join(digic_path, 'wallet_config.json'), wallet_data)

    # User
    click.echo('')
    click.echo(click.style('USER CONFIGURATION', bold=True))
    username = click.prompt('Enter a username', default='Satoshi')
    user.modify_username(new_username=username)
    click.echo(f'Hello {username}!')

    # Wallets
    click.echo('')
    click.echo(click.style('WALLET CONFIGURATION', bold=True))
    click.echo(click.style('Do not enter the PRIVATE keys. Never!', fg='bright_yellow'))

    confirmation = False
    while True:
        if confirmation:
            if not click.confirm('Do you want to add another wallet?'):
                break

        wallet_type = click.prompt('Select a blockchain', type=click.Choice(['bitcoin', 'ethereum']))
        address = click.prompt(f'Enter the {wallet_type} address', type=str)
        label = click.prompt('Enter a name for the address', type=str)
        wallet.add_wallet(wallet_type, label, address)
        confirmation = True

    # APIs
    click.echo('')
    click.echo(click.style('API CONFIGURATION', bold=True))
    click.echo('We use the following APIs to fetch data:')
    click.echo('1) https://etherscan.io')
    click.echo('2) https://blockchain.com')
    click.echo('3) https://coingecko.com')
    etherscan_key = click.prompt('Enter your etherscan.io API key', type=str)
    api.modify_api(vendor='etherscan.io', key=etherscan_key)

    # Reference
    success_message = 'Your configuration settings has been saved correctly!'
    reference_message = 'Source code: https://github.com/denniscm190/digic'

    click.echo('')
    click.echo(click.style(success_message, fg='green'))
    click.echo(click.style(reference_message, italic=True))


cli_group.add_command(init)


"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
                                                    USER COMMANDS                                                                        
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘                
"""


@click.group(name='user')
def user_group():
    """
    manage user data
    """

    pass


@click.command(name='list')
def user_list():
    """
    show username
    """

    username = user.get_username()
    click.echo(f'Username: {username}')


@click.command(name='modify')
@click.option('--username', '-u', type=str, required=True, help='New username')
def user_modify(username):
    """
    modify username
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
    manage API data
    """

    pass


@click.command(name='list')
def api_list():
    """
    show API key
    """

    api_key = api.get_api()
    click.echo(f'etherscan.io: {api_key}')


@click.command(name='modify')
@click.option('--key', '-k', type=str, required=True, help='New API key')
def api_modify(key):
    """
    modify API key
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
    manage wallet data
    """

    pass


@click.command(name='list')
def wallet_list():
    """
    show wallets
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
    add wallet
    """

    wallet.add_wallet(type_, label, address)


@click.command(name='remove')
@click.option('--type', '-t', 'type_', type=click.Choice(['ethereum', 'bitcoin']), required=True, help='blockchain')
@click.option('--label', '-l', type=str, required=True, help='wallet name')
def wallet_remove(type_, label):
    """
    remove wallet
    """

    wallet.remove_wallet(type_, label)


@click.command(name='balance')
@click.option('--type', '-t', 'type_', type=click.Choice(['ethereum', 'bitcoin']), required=True, help='blockchain')
@click.option('--label', '-l', type=str, required=True, help='wallet name')
def wallet_balance(type_, label):
    """
    show wallet balance
    """

    balance = wallet.get_balance_wallet(type_, label)
    click.echo(click.style(f'{type_} wallet'.upper(), bold=True))
    click.echo(f'{label}: {balance[label]}')


cli_group.add_command(wallet_group)
wallet_group.add_command(wallet_list)
wallet_group.add_command(wallet_add)
wallet_group.add_command(wallet_remove)
wallet_group.add_command(wallet_balance)


if __name__ == '__main__':
    cli_group()
