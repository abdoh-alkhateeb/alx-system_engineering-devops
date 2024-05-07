#!/usr/bin/python3
"""
Module that defines recurse.
"""

import requests


def recurse(
    subreddit: str, hot_list: list[str] = [], after: str = ""
) -> list[str] | None:
    """
    Function that returns list containing titles of hot articles for given sub.
    """

    if not isinstance(subreddit, str) or len(subreddit) == 0:
        return None

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) \
            Gecko/20100101 Firefox/123.0"
    }

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers=headers,
        params={"after": after},
        allow_redirects=False,
        timeout=30,
    )

    if response.status_code != 200:
        return None

    try:
        json_response = response.json()
        for child in json_response.get("data", {}).get("children", []):
            data = child.get("data", {})
            title = data.get("title", "")
            hot_list.append(title)

        after = json_response.get("data").get("after")

        if after is None:
            return hot_list or None

        return recurse(subreddit, hot_list, after) or None

    except ValueError:
        return None
