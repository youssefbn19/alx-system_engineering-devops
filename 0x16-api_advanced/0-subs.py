#!/usr/bin/python3
""" Module contains number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Send a request to Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    Args:
        subreddit: subreddit that we want to know its subscribers
    """
    header = {"User-Agent": "Something:)"}
    data = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        allow_redirects=False,
        headers=header,
    )
    if data.status_code == 200:
        dict_data = data.json()
        if dict_data["kind"] == "t5":
            return dict_data["data"]["subscribers"]
    return 0
