#!/usr/bin/python3
"""this modules requests commit data through the Github API."""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    own = sys.argv[2]

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(own, repo))

    values = r.json()
    for item in values:
        print(item.get('sha'), item.get('commit').get('author').
              get('name'))
