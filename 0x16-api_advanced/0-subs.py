#!/usr/bin/python3
"""Module that defines code that returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given sub"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0)\
            Gecko/20100101 Firefox/120.0"
    }
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers=headers)
    try:
        return response.json()["data"]["subscribers"]
    except KeyError:
        return 0
