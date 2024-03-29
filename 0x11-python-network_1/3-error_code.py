#!/usr/bin/python3
""" adjust to error print code """
from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as REQ:
            print(REQ.read().decode("UTF-8"))
    except urllib.error.HTTPError as Err:
        print(f"Error code: {Err.code}")
