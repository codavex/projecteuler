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

    i = 1
    j = 2
    summation = 0
    while j < limit:
        summation += j
        i, j = j, i+j  # odd
        i, j = j, i+j  # odd
        i, j = j, i+j  # even

    print(summation)


if __name__ == "__main__":
    main(sys.argv[1:])
