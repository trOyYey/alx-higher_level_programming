#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > len(my_list) - 1):
        return my_list
    else:
        clone_list = my_list.copy()
        clone_list[idx] = element
        return clone_list
