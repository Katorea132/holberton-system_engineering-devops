#!/usr/bin/python3
"""Entire hot list"""

import requests


def recurse(subreddit, hot_list=[], after="Start"):
    """Returns entire hot list

    Args:
        subreddit (string): Subreddit name
        hot_list (list): List of titles
    """
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; \
               rv:80.0) Gecko/20100101 Firefox/80.0"}
    params = {'limit': 100, 'after': None}
    if after:
        if after != "Start":
            params['after'] = after
        else:
            params['after'] = None
    else:
        return hot_list
    ans = requests.get(url, headers=headers, params=params)
    if ans.status_code == 200:
        ans = ans.json().get('data')
        after = ans.get('after')
        ans = ans.get('children')
        for hot in ans:
            hot_list.append(hot.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        return None
