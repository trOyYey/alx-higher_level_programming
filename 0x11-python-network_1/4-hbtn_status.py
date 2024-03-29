#!/usr/bin/python3
""" script fetches https://alx-intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    request = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(request)}")
    print(f"\t- content: {request}")
