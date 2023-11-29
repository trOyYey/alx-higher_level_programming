#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        j = ""
        if (i % 3 == 0):
            j += "Fizz"
        if (i % 5 == 0):
            j += "Buzz"
        print("{}".format(j if len(j) else i), end=" ")
