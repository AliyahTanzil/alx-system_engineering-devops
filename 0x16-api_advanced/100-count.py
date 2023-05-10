from request import get


"""
This function will count all words
"""
def count_words(subreddit, word_list, count_dict=None):
    if not count_dict:
        count_dict = {}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return
    data = response.json()
    if not data['data']['children']:
        return
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title and not any([char.isalpha() for char in title[title.find(word)+len(word)]]):
                if word.lower() in count_dict:
                    count_dict[word.lower()] += 1
                else:
                    count_dict[word.lower()] = 1
    if not data['data']['after']:
        sorted_words = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print('{}: {}'.format(word, count))
        return
    else:
        return count_words(subreddit, word_list, count_dict=count_dict)
