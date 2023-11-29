#!/usr/bin/python3
def uppercase(str):
    for c in str:
        v = c
        if (ord(v) >= ord('a') and ord(v) <= ord('z')):
            v = chr(ord(c) - ord('a') + ord('A'))
        print("{}".format(v), end="")
    print("{}".format("\n"), end="")
