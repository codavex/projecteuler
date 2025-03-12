#!/bin/python3

import getopt
import sys


def main(argv):
    limit = None
    usage = f"{sys.argv[0]} -l <limit>"

    try:
        opts, _ = getopt.getopt(argv, "l:", ["limit="])
    except getopt.GetoptError:
        print(usage)
        sys.exit()

    # sort out options
    try:
        for opt, arg in opts:
            if opt in ("-l", "--limit"):
                limit = int(arg)
        if limit is None:
            raise ValueError("Limit not set")
    except ValueError:
        print(usage)
        sys.exit()

    largest_factor = 0
    factor = 2
    while limit > 1:
        while limit % factor == 0:
            largest_factor = factor
            limit = limit / factor
        factor += 1

    print(largest_factor)


if __name__ == "__main__":
    main(sys.argv[1:])
