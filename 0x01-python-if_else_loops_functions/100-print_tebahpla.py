#!/usr/bin/python3

for i in range(26):
    c = chr(25 - i + ord('A'))
    if ((25 - i) % 2 != 0):
        c = chr(ord(c) + ord('a') - ord('A'))
    print('{}'.format(c), end='')
