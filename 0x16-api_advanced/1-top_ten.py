#!/usr/bin/python3
"""
Module that defines top_ten.
"""

import requests


def top_ten(subreddit: str) -> None:
    """
    Function that prints titles of first 10 hot posts listed for a given sub.
    """

    if not isinstance(subreddit, str) or len(subreddit) == 0:
        print(None)
        return

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) \
            Gecko/20100101 Firefox/123.0"
    }

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers=headers,
        params={"limit": 10},
        allow_redirects=False,
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        for child in response.json().get("data", {}).get("children", []):
            data = child.get("data", {})
            title = data.get("title", "")
            print(title)
    except ValueError:
        print(None)
