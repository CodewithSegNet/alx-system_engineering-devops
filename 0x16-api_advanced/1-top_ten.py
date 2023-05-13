#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of the first 10 hot posts listed"""

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

    params = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        for entry in data.get('children'):
            print(entry.get('data').get('title'))
    else:
        print("None")
        return
