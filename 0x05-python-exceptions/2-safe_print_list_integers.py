#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    y, i = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            y += 1
        except (TypeError, ValueError):
            None
        i += 1
    print()
    return y
