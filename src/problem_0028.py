#!/bin/python3

""" https://projecteuler.net/problem=28 """

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

    limit = limit * limit
    summation = 1
    jump = 2
    val = 3
    while val < limit:
        summation, val = summation + val, val + jump
        summation, val = summation + val, val + jump
        summation, val = summation + val, val + jump
        summation, val = summation + val, val + jump + 2
        jump += 2
    print(summation)


if __name__ == "__main__":
    main(sys.argv[1:])
