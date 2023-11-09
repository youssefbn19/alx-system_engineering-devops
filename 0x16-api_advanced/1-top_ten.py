#!/usr/bin/python3
"""
    The Module queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    The titles of the first 10 hot posts
    listed for a given subreddit.
    """
    import requests
    header = {"User-Agent": "ChibiTech/1.0"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    sub = requests.get(url, headers=header)
    if sub.ok:
        data = sub.json()
        if data['data']['children']:
            for post in data['data']['children']:
                print(post['data']['title'])
            return
    print('None')
