import json
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/.config'.format(dir_path)


def init_username(username):
    with open('{}/user_data.json'.format(config_path), 'w') as user_file:
        user_data = {'username': username}
        json.dump(user_data, user_file)


def get_username():
    with open('{}/user_data.json'.format(config_path)) as user_file:
        user_data = json.load(user_file)
        username = user_data['username']

    return username


def modify_username(new):
    with open('{}/user_data.json'.format(config_path), 'w') as user_file:
        user_data = {'username': new}
        json.dump(user_data, user_file)
