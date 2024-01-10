#!/usr/bin/python3
'''reading from json, adding args and saving them'''


import sys
load_json = __import__('6-load_from_json_file').load_from_json_file
save_json = __import__('5-save_to_json_file').save_to_json_file

arguments = list(sys.argv[1:])
try:
    data = load_json('add_item.json')
except Exception:
    data = []

data.extend(arguments)
save_json(data, 'add_item.json')
