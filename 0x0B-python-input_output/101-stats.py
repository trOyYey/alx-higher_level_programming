#!/usr/bin/python3
"""
reads STDIN line by line :

"""
import sys


def print_stat(size, stats):
    """prints stats in specified format"""
    f_size = "File size: {}\n".format(size)
    for x in stats:
        if stats[x] != 0:
            f_size += "{}: {}\n".format(x, stats[x])
    sys.stdout.write(f_size)
    sys.stdout.flush()


def main():
    size = 0
    stats = {"200": 0, "301": 0, "400": 0,
             "401": 0, "403": 0, "404": 0,
             "405": 0, "500": 0}
    count = 0

    def process_line(line):
        nonlocal size, count
        try:
            split = line[:-1].split()[-2:]
            size += int(split[-1])
            if split[0] in stats:
                stats[split[0]] += 1
        except Exception:
            pass
        count += 1

        if count % 10 == 0:
            print_stat(size, stats)

    try:
        for line in sys.stdin:
            process_line(line)
        print_stat(size, stats)
    except KeyboardInterrupt:
        print_stat(size, stats)
        raise


if __name__ == "__main__":
    main()
