#!/usr/bin/python3
"""
Function that returns the number of subscribers of a 
given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """ queries a subbreddit and returns the number of subs
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url,allow_redirects=False, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
