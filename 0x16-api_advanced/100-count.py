#!/usr/bin/python3
'''recursive function that queries
the Reddit API, parses the title of
all hot articles, and prints
'''
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    '''recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints'''
    headers = {'User-Agent': 'Agent'}
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code != 200:
        return
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    after = data.get("data", {}).get("after")
    if after is None:
        word_ct = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in word_ct:
            print(f"{word}: {count}")
        return
    else:
        return count_words(subreddit, word_list, after, word_count)
