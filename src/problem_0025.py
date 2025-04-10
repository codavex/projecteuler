#!/bin/python3

""" https://projecteuler.net/problem=25 """

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

    i, j = 1, 1
    k = 2
    while len(str(j)) < limit:
        i, j = j, j + i
        k += 1

    print(k)


if __name__ == "__main__":
    main(sys.argv[1:])
