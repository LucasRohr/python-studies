import requests


def get_thing():
    result = requests.get('http://localhost/api/get')

    if result.status_code == 200:
        return result.json()
    return None