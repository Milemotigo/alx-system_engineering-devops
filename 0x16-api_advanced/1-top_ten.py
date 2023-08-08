#!/usr/bin/env python3
"""function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given
"""
import requests


def top_ten(subreddit):
    """top ten hotest posts"""
    headers = {'User-Agent': 'FApi'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_codes == 200:
        return response
    else:
        return 0