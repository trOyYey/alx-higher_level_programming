#!/usr/bin/python3
from sys

def main():
    Len = len(argv)
    argu = "argument" if Len == 2 else "arguments"
    if (Len == 1):
        print(f"0 {argu}.")
    else:
        print(f"{Len - 1} {argu}:")
        for i in range(1, Len):
            print(f"{i}: {argv[i]}")


if __name__ == "__main__":
    main()
