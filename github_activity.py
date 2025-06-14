from http import HTTPStatus
import sys
import requests


def fetch_events(data):
    pass


def call_api(username):
    if not username:
        return

    github_api = f'https://api.github.com/users/{username}/events'
    response = requests.get(github_api)

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        fetch_events(data)
    else:
        print(response.json)


def main(username):
    call_api(username)    


if __name__ == '__main__':
    username = sys.argv[1]
    main(username)
