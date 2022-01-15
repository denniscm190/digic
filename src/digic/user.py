from pathlib import Path
from digic import utils

digic_path = str(f'{Path.home()}/.digic')


def get_username():
    """
    Get username
    :return: str
    """

    user_data = utils.read_json(path=f'{digic_path}/user_config.json')

    return user_data['username']


def modify_username(new_username):
    """
    Modify current username
    :param new_username: str, required
    :return: None
    """

    user_data = {'username': new_username}
    utils.write_json(path=f'{digic_path}/user_config.json', data=user_data)
