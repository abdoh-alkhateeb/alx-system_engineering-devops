#!/usr/bin/python3
"""Returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0)\
            Gecko/20100101 Firefox/120.0"
    }

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers=headers,
        allow_redirects=False,
    )

    if response.status_code != 200:
        return 0

    return response.json()["data"]["subscribers"]
