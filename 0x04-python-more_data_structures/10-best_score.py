#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return sorted(a_dictionary.items(), key=lambda a: a[1])[-1][0]
