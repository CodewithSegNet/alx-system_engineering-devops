#!/usr/bin/python3
"""Exporting CSV files"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers."""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.82 Safari/537.36"
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")

    return 0
