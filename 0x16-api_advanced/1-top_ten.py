#!/usr/bin/python3
"""
This module defines the number_of_subscribers function.
"""
import requests


def top_ten(subreddit):
    # Set the URL and parameters for the API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}

    # Set the headers to include the user agent
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Send the request and get the response
    response = requests.get(url, params=params, headers=headers)

    # Check the status code of the response
    if response.status_code != 200:
        print(None)
        return

    # Parse the JSON data from the response
    data = response.json()

    # Print the titles of the first 10 posts
    for i in range(10):
        print(data['data']['children'][i]['data']['title'])

