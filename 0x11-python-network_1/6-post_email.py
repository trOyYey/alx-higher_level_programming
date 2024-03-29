#!/usr/bin/python3
""" sends a POST request and displays thre body"""
import requests
from sys import argv


if __name__ == "__main__":
    request = requests.post(argv[1], data={"email": argv[2]}).text
    print(f"{request}")
