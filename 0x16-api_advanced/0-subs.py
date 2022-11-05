#!/usr/bin/python3

"""API REDIT
"""
import request

def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0."""
    baseUrl = 'https://www.reddit.com/r/'
    url = baseUrl + subreddit + "/about.json"
    agent = {'User-Agent': "mad01"}
    response = requests.get(url, headers=agent, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
