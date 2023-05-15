#!/usr/bin/pyhton3
"""Write a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords"""

import json
import requests


def count_words(subreddit, word_list, after="", counts=None):
    if counts is None:
        counts = {}
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.82 Safari/537.36"
    }

    params = {"after": after, "limit": 100}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        for entry in results.get("children"):
            title = entry.get("data").get("title").lower()
            for word in word_list:
                if word.lower() in title.split():
                    counts[word] = counts.get(word, 0) + 1
        
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word.lower(), count))
    
    return None
