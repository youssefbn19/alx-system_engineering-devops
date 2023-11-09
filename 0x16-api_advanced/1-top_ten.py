#!/usr/bin/python3
"""
    The Module queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
"""


def top_ten(sub):
    """
    The titles of the first 10 hot posts
    listed for a given subreddit.
    """
    import requests
    header = {"User-Agent": "ChibiTech/1.0"}
    sub = requests.get(f'https://www.reddit.com/r/{sub}/hot.json?limit=10',
                       headers=header)
    if sub.ok:
        data = sub.json()
        if data['data']['children']:
            for post in data['data']['children']:
                print(post['data']['title'])
            return
    print('None')
