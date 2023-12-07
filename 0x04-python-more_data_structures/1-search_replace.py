#!/usr/bin/python3

def search_replace(my_list, search, replace):
    clone = []
    if my_list:
        for i in my_list:
            if i == search:
                clone.append(replace)
            else:
                clone.append(i)
    return (clone)
