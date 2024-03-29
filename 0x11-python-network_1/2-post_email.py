#!/usr/bin/python3
""" Post request with URL and Email args and display body of response """
from sys import argv
import urllib.request


if __name__ == "__main__":
    email = urllib.parse.urlencode({"email": argv[2]}).encode('ascii')
    post_req = urllib.request.Request(argv[1], email)
    with urllib.request.urlopen(post_req) as REQ:
        print(REQ.read().decode("UTF-8"))
