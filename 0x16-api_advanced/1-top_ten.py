#!/usr/bin/python3
"""
Queries api for the top 10 hot posts of a given subreddit
"""

import requests

def top_ten(subreddit):
    # Define the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set the user-agent header to avoid issues with Reddit's API
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        # Print the titles of the top 10 hot posts
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
