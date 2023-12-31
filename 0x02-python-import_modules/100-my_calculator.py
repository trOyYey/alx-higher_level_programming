#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

def main():
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    x = int(argv[1])
    z = int(argv[3])
    if (argv[2] == '+'):
        print("{:d} + {:d} = {:d}".format(x, z, add(x, z)))
    elif (argv[2] == '-'):
        print("{:d} - {:d} = {:d}".format(x, z, sub(x, z)))
    elif (argv[2] == '*'):
        print("{:d} * {:d} = {:d}".format(x, z, mul(x, z)))
    elif (argv[2] == '/'):
        print("{:d} / {:d} = {:d}".format(x, z, div(x, z)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

if __name__ == "__main__":
    main()
