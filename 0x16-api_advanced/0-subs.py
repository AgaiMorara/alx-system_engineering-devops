#!/usr/bin/python3
"""Function to Querry Reddit API and return the number of subscribers"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API,
    Returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    data = requests.get(info, allow_redirects=False,
                        headers=headers)
    if str(data) == "<Response [200]>":
        data_json = data.json()
        return data_json.get("data").get("subscribers")
    return 0
