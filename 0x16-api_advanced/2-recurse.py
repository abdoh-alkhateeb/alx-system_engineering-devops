#!/usr/bin/python3
"""Returns a list containing the titles of all hot articles"""
import requests
from time import sleep


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0)\
            Gecko/20100101 Firefox/120.0"
    }

    params = {
        "after": after,
        "limit": "100"
    }

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    after = response.json()["data"]["after"]
    for child in response.json()["data"]["children"]:
        hot_list.append(child["data"]["title"])

    if after is None:
        return hot_list
    else:
        sleep(2)
        return recurse(subreddit, hot_list, after)
