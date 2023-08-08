#!/usr/bin/python3
""" a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """gets the number of subscribers"""
    headers = {'User-Agent': 'FApi'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        allData = data["data"]['subscribers']
        return allData

    else:
        return 0