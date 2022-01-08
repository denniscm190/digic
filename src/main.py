import os
import click
import utils
import user_methods
import wallet_methods
import api_methods

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


@click.group()
def cli():
    """
    A privacy focused command line tool to track your crypto portfolio
    """
    pass


@click.command()
def init():
    """
    Set up Digic for the first time
    """

    try:
        os.mkdir(config_path)
    except FileExistsError:
        warning = click.style('This action will reset the app data. Do you want to continue?', fg='red')
        click.confirm(warning, abort=True)

    # User
    click.echo('')
    click.echo(click.style('USER CONFIGURATION', bold=True))
    username = click.prompt('Enter a username', default='Satoshi')
    user_methods.init_username(username)
    click.echo('>>> Hello {}! Now let\'s set up your wallets'.format(username))

    # Wallets
    click.echo('')
    click.echo(click.style('WALLET CONFIGURATION', bold=True))
    click.echo('>>> Add the public keys to follow')
    click.echo(click.style('>>> Do not enter your PRIVATE keys. Never!', fg='bright_yellow'))
    wallet_type = click.prompt('Select a blockchain', type=click.Choice(['bitcoin', 'ethereum']))
    address = click.prompt('Enter your {} address'.format(wallet_type), type=str)
    label = click.prompt('How do we name your address?', type=str)
    wallet_methods.init_wallet(wallet_type, label, address)

    while click.confirm('Do you want to add another wallet?'):
        wallet_type = click.prompt('Select a blockchain', type=click.Choice(['bitcoin', 'ethereum']))
        address = click.prompt('Enter your {} address'.format(wallet_type), type=str)
        label = click.prompt('How do we name your address?', type=str)
        wallet_methods.add_wallet(wallet_type, label, address)

    # APIs
    click.echo('')
    click.echo(click.style('API CONFIGURATION', bold=True))
    click.echo('>>> To fetch blockchain data we use the following APIs')
    click.echo('>>> 1) https://docs.etherscan.io')
    click.echo('>>> 2) https://www.blockchain.com/es/api/blockchain_api')
    click.echo('>>> 3) https://www.coingecko.com/es/api/documentation?')
    click.echo('>>> In order to use etherscan.io we need your api key')
    etherscan_key = click.prompt('Enter the etherscan.io key', type=str)
    api_methods.init_api('etherscan.io', etherscan_key)
    click.echo('>>> Testing APIs...')
    blockchain_url = 'https://blockchain.info/rawblock/00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048'
    coingecko_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin'
    etherscan_url = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=1&apikey={}'.format(
        etherscan_key
    )

    utils.call_api(blockchain_url)
    click.echo(click.style(u'>>> \u2713 blockchain.com', fg='green'))
    utils.call_api(coingecko_url)
    click.echo(click.style(u'>>> \u2713 coingecko.com', fg='green'))
    utils.call_api(etherscan_url)
    click.echo(click.style(u'>>> \u2713 etherscan.io', fg='green'))

    success_message = '>>> Your configuration settings has been saved correctly!'
    help_message = '>>> Enter the --help command if you need guidance using digic'
    reference_message = '>>> Digic is an open source privacy focused command line tool to track your crypto ' \
                        'portfolio.\n>>> Consider contributing to the project https://github.com/denniscm190/digic\n'

    click.echo('')
    click.echo(click.style(success_message, fg='green'))
    click.echo(help_message)
    click.echo(click.style(reference_message, bold=True))


##
# USER GROUP
##


@click.group()
def user():
    """
    Manage user data
    """

    pass


@click.command(name='show')
def user_show():
    """
    Get username
    """

    username = user_methods.get_username()
    click.echo('{}: {}'.format(
        click.style('Username', bold=True),
        username
    ))


@click.command(name='modify')
def user_modify():
    """
    Modify username
    """

    new = click.prompt('Enter a new username', default='Satoshi')
    user_methods.modify_username(new)


##
# WALLET GROUP
##


@click.group()
def wallet():
    """
    Manage wallet data
    """

    pass


@click.command(name='show')
def wallet_show():
    """
    Get wallets
    """

    wallet_data = wallet_methods.get_wallet_data()
    for wallet_type in wallet_data:
        click.echo(click.style('{} wallets'.upper().format(wallet_type.upper()), bold=True))
        for wallet_dict in wallet_data[wallet_type]:
            for label in list(wallet_dict.keys()):
                address = wallet_dict[label]
                click.echo('> {}: {}'.format(click.style(label, bold=True), address))


cli.add_command(init)
cli.add_command(user)
cli.add_command(wallet)
user.add_command(user_show)
user.add_command(user_modify)
wallet.add_command(wallet_show)


if __name__ == '__main__':
    cli()
