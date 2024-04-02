#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to search_user """
import requests
from sys import argv


if __name__ == "__main__":
    q = {"q": "" if len(argv) == 1 else argv[1]}
    request = requests.post("http://0.0.0.0:5000/search_user", data=q)
    if '{' and '}' in request.text:
        json = request.json()
        if len(json) == 0:
            print("No result")
        else:
            print(f"[{json.get('id')}] {json.get('name')}")
