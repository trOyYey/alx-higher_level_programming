#!/usr/bin/python3

from sys import argv

def main():
    result = 0
    for number in argv[1:]:
        result += int(number)
    print(result)


if __name__ == "__main__":
    main()
