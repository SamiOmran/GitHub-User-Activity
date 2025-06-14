from http import HTTPStatus
import sys
import requests


def get_type(event):
    return event.get('type')


def get_repo_name(event):
    repo = event.get('rep')
    if repo:
        return repo.get('name')


def display_result(map):
    print('Output: \n')
    for key, value in map.items():
        print(f'- {value}  {key}')


def fetch_events(data):
    event_map = {
        'PullRequestEvent': 0,
        'CommitCommentEvent': 0,
        'CreateEvent': 0,
        'DeleteEvent': 0,
        'ForkEvent': 0,
        'GollumEvent': 0,
        'IssueCommentEvent': 0,
        'IssuesEvent': 0,
        'MemberEvent': 0,
        'PublicEvent': 0,
        'PullRequestReviewEvent': 0,
        'PullRequestReviewCommentEvent': 0,
        'PullRequestReviewThreadEvent': 0,
        'PushEvent': 0,
        'ReleaseEvent': 0,
        'SponsorshipEvent': 0,
        'WatchEvent': 0
    }

    for event in data:
        type = get_type(event)
        event_map[type] += 1

    display_result(event_map)


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
