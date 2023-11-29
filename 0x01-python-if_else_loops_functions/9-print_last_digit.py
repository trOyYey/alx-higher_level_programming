#!/usr/bin/python3

def print_last_digit(number):
    L = abs(number) % 10
    print(L, end="")
    return L
