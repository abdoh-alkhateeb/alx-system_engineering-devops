#!/usr/bin/python3
"""
Module that defines number_of_subscribers.
"""

import requests


def number_of_subscribers(subreddit: str) -> int:
    """
    Function that returns the number of subscribers for a given subreddit.
    """

    if not isinstance(subreddit, str) or len(subreddit) == 0:
        return 0

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) \
            Gecko/20100101 Firefox/123.0"
    }

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers=headers,
        allow_redirects=False,
    )

    if response.status_code != 200:
        return 0

    try:
        return response.json().get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
