#!/bin/python3

""" https://projecteuler.net/problem=6 """

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

    summation = int(limit * (limit + 1) / 2)
    sum_of_squares = int(((2*limit) + 1)*(limit + 1)*limit/6)
    print((summation*summation) - sum_of_squares)


if __name__ == "__main__":
    main(sys.argv[1:])
