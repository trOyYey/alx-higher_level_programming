#!/usr/bin/python3
""" same as task 6 with edition to error handling """
import requests
from sys import argv


if __name__ == "__main__":
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        print(f"{request.text}")
