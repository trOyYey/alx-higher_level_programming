#!/usr/bin/python3

for numb in range(100):
    if (numb == 89):
        print('{:d}'.format(numb))
    elif numb < int(numb / 10) + numb % 10 * 10:
        print('{:02d}'.format(numb), end=", ")
