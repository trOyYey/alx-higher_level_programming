#!/usr/bin/python3
"""def save_to_json_file funtion mod"""
import json


def save_to_json_file(my_obj, filename):
    """write the json into object to a file"""
    with open(filename, "w+", encoding='utf-8') as datafile:
        datafile.write(json.dumps(my_obj))
