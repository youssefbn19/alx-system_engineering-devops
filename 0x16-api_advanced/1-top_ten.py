#!/usr/bin/python3
""" Module contains top_ten function
"""

import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
        Args:
            subreddit: subreddit that we want to prints the titles of
            the first 10 hot posts
    """
    header = {"User-Agent": "Something:)"}
    data = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        allow_redirects=False,
        headers=header,
    )
    if data.status_code == 200:
        dict_data = data.json()
        posts = dict_data["data"]["children"]
        number_posts = 10
        if posts:
            if len(posts) < 10:
                number_posts = len(posts)
            for i in range(0, number_posts):
                print(posts[i]["data"]["title"])
            return
    print(None)
