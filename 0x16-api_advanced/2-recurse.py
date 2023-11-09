#!/usr/bin/python3
"""
    The Module that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should return None.
"""


def recurse(subreddit, after = None, hot_list=[]):
    """
    List containing the titles of all hot
    articles for a given subreddit.
    """
    import requests
    header = {"User-Agent": "CustomUser/1.0"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    sub = requests.get(url, headers=header, allow_redirects=False)
    if sub.ok:
        data = sub.json()
        if data['data']['children']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            recurse(subreddit, after, hot_list)
        return hot_list
    return None
