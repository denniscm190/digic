import requests


def call_api(url):
    response = requests.get(url)
    status = response.status_code
    if response.status_code == 200:
        result = response.json()
    else:
        raise Exception('ERROR: {} -- URL: {} -- STATUS: {}'.format(response.text, url, status))

    return result
