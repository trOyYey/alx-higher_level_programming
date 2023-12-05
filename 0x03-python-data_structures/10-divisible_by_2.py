#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    even = []
    for i in my_list:
        even.append(True if i % 2 == 0 else False)
    return even
