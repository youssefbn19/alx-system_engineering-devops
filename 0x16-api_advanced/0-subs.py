#!/usr/bin/python3
""" Module contains number_of_subscribers function
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    Send a request to Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    Args:
        subreddit: subreddit that we want to know its subscribers
    """
    data = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
    if data.status_code == 200:
        dict_data = json.loads(data.text)
        if dict_data["kind"] == "t5":
            return dict_data["data"]["subscribers"]
    return 0
