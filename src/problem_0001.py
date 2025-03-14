#!/bin/python3

""" https://projecteuler.net/problem=1 """

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

    print(sum_divisible_by(limit, 3) +
          sum_divisible_by(limit, 5) -
          sum_divisible_by(limit, 15))


def sum_divisible_by(limit, i):
    j = int((limit-1) / i)
    return int(i*(j*(j+1)) / 2)


if __name__ == "__main__":
    main(sys.argv[1:])
