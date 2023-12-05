#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    z = [0, 0]
    for y in range(len(tuple_a[:2])):
        z[y] += tuple_a[y]
    for x in range(len(tuple_b[:2])):
        z[x] += tuple_b[x]
    return (z[0], z[1])
