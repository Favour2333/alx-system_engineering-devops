#!/usr/bin/python3
"""
This module defines the number_of_subscribers function.
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively get all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        for child in children:
            hot_list.append(child["data"]["title"])
        after = data["data"]["after"]
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None


