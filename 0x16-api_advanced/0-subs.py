#!/usr/bin/python3
"""
    The Module queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
"""


def number_of_subscribers(subreddit):
    """
    The number of subscribers (not active users,
    total subscribers) for a given.
    """
    import requests
    header = {"User-Agent": "ChibiTech/1.0"}
    sub = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                       headers=header)
    if sub.ok:
        data = sub.json()
        if data['kind'] == 't5':
            return data['data']['subscribers']
    return 0
