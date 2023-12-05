#!/usr/bin/python3


def max_integer(my_list=[]):
    biggest = None if len(my_list) == 0 else my_list[0]
    for i in my_list:
        biggest = i if i > biggest else biggest
    return biggest
