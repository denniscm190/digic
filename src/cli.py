import os
import utils
import click
import shutil
import api
import user
import wallet

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


@click.group(name='cli')
def cli_group():
    """
    A privacy focused command line tool to track your crypto portfolio
    """

    pass


"""
CONFIGURATION
"""


@click.command()
def init():
    """
    Set up Digic for the first time
    """

    # Create files
    os.mkdir(config_path)
    user_data = {'username': ''}
    api_data = {'etherscan.io': ''}
    wallet_data = {'ethereum': [], 'bitcoin': []}
    utils.write_json(f'{config_path}/user_data.json', user_data)
    utils.write_json(f'{config_path}/api_data.json', api_data)
    utils.write_json(f'{config_path}/wallet_data.json', wallet_data)

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
    api.add_api(vendor='etherscan.io', key=etherscan_key)
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


@click.command()
def reset():
    """
    Reset configuration
    """

    shutil.rmtree(config_path, ignore_errors=True)


"""
USER
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


cli_group.add_command(init)
cli_group.add_command(reset)
cli_group.add_command(user_group)
user_group.add_command(user_list)
user_group.add_command(user_modify)


if __name__ == '__main__':
    cli_group()
