#!/usr/bin/python3
"""Gets 10 hots"""

import requests


def top_ten(subreddit):
    """Prints 10 hot titles

    Args:
        subreddit (string): Subreddit name
    """
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; \
               rv:80.0) Gecko/20100101 Firefox/80.0"}
    ans = requests.get(url, headers=headers)
    if ans.status_code == 200:
        ans = ans.json().get('data').get('children')
        for _, lili in zip(range(0, 10), ans):
            print(lili.get('data').get('title'))
    else:
        print("None")
