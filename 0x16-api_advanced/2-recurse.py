#!usr/bin/python3
from requests import get


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    url = 'https://www.reddit.com/r/{subreddit}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for child in children:
            hot_list.append(child['data']['title'])
        if data['data']['after']:
            recurse(subreddit, hot_list, data['data']['after'])
        return hot_list
    else:
        return None
