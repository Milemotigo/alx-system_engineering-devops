#!/usr/bin/python3
'''recursion'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''recusion function'''
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {'User-Agent': '2-recursive'}
    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    if not posts:
        return None
    for post in posts:
        hot_list.append(post["data"]["title"])
    after = data.get("data", {}).get("after")
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
