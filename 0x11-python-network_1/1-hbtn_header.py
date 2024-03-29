#!/usr/bin/python3
""" sends request to url and prints X-Request-Id """
from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as request:
        response = request.info()
        print(response.get("X-Request-Id"))
