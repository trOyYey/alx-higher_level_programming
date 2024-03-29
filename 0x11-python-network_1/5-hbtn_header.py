#!/usr/bin/python3
""" displays the value of the variable X-Request-Id from response"""
import requests
from sys import argv

if __name__ == "__main__":
    request = requests.get(argv[1])
    print(request.headers.get("X-Request-Id"))
