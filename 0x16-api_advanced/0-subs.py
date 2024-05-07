#!/usr/bin/python3
"""
Module that defines number_of_subscribers.
"""

import requests


def number_of_subscribers(subreddit: str) -> int:
    """
    Function that returns the number of subscribers for a given subreddit.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) \
            Gecko/20100101 Firefox/123.0"
    }

    response = requests.get(
        f"http://www.reddit.com/r/{subreddit}/about.json", headers=headers
    )

    if response.status_code != 200:
        return 0

    return response.json().get("data", {}).get("subscribers", 0)
