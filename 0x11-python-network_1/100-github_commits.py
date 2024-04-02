#!/usr/bin/python3
""" github commits"""
import requests
from sys import argv


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    limit = {"per_page": 10}
    header = {"X-GitHub-Api-Version": "2022-11-28"}
    request = requests.get(url, params=limit, headers=header).json()
    for key in request:
        print("{key.get('sha')}: {key.get('commit').get('author').get('name')}")
