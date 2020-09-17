#!/usr/bin/python3
"""Gets subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Returns amount of subscribers

    Args:
        subreddit (string): Subreddit name 

    Returns:
        int: Amount of subscribers
    """
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; \
               rv:80.0) Gecko/20100101 Firefox/80.0"}
    ans = requests.get(url, headers=headers)
    if ans.status_code == 200:
        return ans.json().get('data').get('subscribers')
    return 0
