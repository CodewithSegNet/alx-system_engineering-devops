import requests

def count_words(subreddit, word_list):
    """Count the titles found with wordlist in subreddit"""
    my_dict = {}

    for word in word_list:
        my_dict[word] = 0

    hot_list = recurse(subreddit)

    if hot_list:
        for title in hot_list:
            for word in word_list:
                if word.lower() in title.lower():
                    my_dict[word] += 1

    for key, val in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
        if val != 0:
            print("{}: {}".format(key, val))

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches hot titles from a subreddit"""
    headers = {'user-agent': 'mobile-device'}
    params = {'after': after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False, params=params)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            after = data.get('after')
            children = data.get('children')
            if children:
                for child in children:
                    title = child.get('data').get('title')
                    hot_list.append(title)
            if after:
                recurse(subreddit, hot_list, after)

    return hot_list
