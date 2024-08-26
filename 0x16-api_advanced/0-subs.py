#!/usr/bin/python3
"""Function to Querry Reddit API and return the number of subscribers"""

import json
import requests
import sys

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API,
    Returns the number of subscribers
    """
    headers = {'user-agent': 'Requests'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False,headers=headers)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)
