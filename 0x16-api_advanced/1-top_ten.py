#!/usr/bin/python3
"""A function that queries the Reddit API and \
        prints the titles of the first 10 hot posts listed"""

import json
import requests


def top_ten(subreddit):
    """Query the Reddit API"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.82 Safari/537.36"
    }

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        for a in list_titles[:10]:
            print(a['data']['title'])
    else:
        return(print("None"))
