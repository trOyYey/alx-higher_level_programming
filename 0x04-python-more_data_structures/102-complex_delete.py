#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    r = []
    for key, val in a_dictionary.items():
        if value == val:
            r.append(key)
    del a_dictionary[r]
    return a_dictionary
