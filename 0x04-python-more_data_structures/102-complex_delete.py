#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    r = []
    for key, val in a_dictionary.items():
        if value == val:
            r.append(key)
    for u in r:
        del a_dictionary[u]
    return a_dictionary
