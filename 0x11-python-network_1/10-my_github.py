#!/usr/bin/python3
""" get and print id of github using name and pass as args """
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(argv[1], argv[2])
    header = {"X-GitHub-Api-Version": "2022-11-28"}

    request = requests.get(url, auth=auth, headers=header)
    if '{' and '}' in request.text:
        print(request.json().get("id"))
    else:
        print(None)
