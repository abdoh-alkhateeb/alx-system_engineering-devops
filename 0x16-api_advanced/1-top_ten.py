#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0)\
            Gecko/20100101 Firefox/120.0"
    }
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    for child in response.json()["data"]["children"][:10]:
        print(child["data"]["title"])
