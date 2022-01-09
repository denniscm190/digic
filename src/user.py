import os
import utils

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def get_username():
    """
    Get username
    :return: str
    """

    user_data = utils.read_json(path=f'{config_path}/user_data.json')

    return user_data['username']


def modify_username(new_username):
    """
    Modify current username
    :param new_username: str, required
    :return: None
    """

    user_data = {'username': new_username}
    utils.write_json(path=f'{config_path}/user_data.json', data=user_data)
