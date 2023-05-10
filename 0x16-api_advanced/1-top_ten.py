#!usr/bin/python3
from requests import get


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{subreddit}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
