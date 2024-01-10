#!/usr/bin/python3
"""def load_from_json_file funtion mod"""
import json


def load_from_json_file(filename):
    """load json from a specified file"""
    with open(filename, encoding='utf-8') as datafile:
        return json.loads(datafile.read())
