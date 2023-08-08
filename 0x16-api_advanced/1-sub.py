import requests

def number_of_subscribers(subreddit):
    """Gets the number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'FApi'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"  # Include the correct subreddit parameter
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:  # Check the status code using .status_code
        data = response.json()
        return data
    else:
        return 0

if __name__ == '__main__':
    subreddit_name = 'programming'  # Pass a valid subreddit name
    print(number_of_subscribers(subreddit_name))
