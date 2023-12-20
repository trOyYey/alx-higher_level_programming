#!/usr/bin/python3

def magic_calculation(a, b):
    y = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                y += a ** b / x
        except Exception:
            y = a + b
            break
    return y
