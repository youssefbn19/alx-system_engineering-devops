#!/usr/bin/python3
""" Module contains recurse function
"""

import requests


def recurse(subreddit, hot_list=[], after_str=""):
    """
    a recursive function that queries the Reddit API and
    returns a list containing the titles of
    all hot articles for a given subreddit.
        Args:
            subreddit: subreddit text
            hot_list: list of the titles of all hot article
    """
    header = {"User-Agent": "Something:)"}
    data = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?after={after_str}",
        allow_redirects=False,
        headers=header,
    )
    if data.status_code == 200:
        data_dict = data.json()
        if data_dict["data"]["children"]:
            for obj in data_dict["data"]["children"]:
                hot_list.append(obj["data"]["title"])

        if data_dict["data"]["after"]:
            recurse(subreddit, hot_list, data_dict["data"]["after"])
        return hot_list
    return None
