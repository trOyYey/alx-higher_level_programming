#!/usr/bin/python3
"""read from json, add the arguments, save it in file"""


import sys
load_from_json = __import__('6-load_from_json_file').load_from_json_file
save_to_json = __import__('5-save_to_json_file').save_to_json_file


def main():
    filename = "add_item.json"
    try:
        lst = load_from_json(filename)
    except FileNotFoundError:
        lst = []

    for i in sys.argv[1:]:
        lst.append(i)

    save_to_json(lst, filename)


if __name__ == "__main__":
    main()
