#!/bin/python3

""" https://projecteuler.net/problem=12 """

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

    triangle = 0
    i = 0
    while True:
        i += 1
        triangle += i
        divisors = 0
        for j in range(1, triangle + 1):
            if triangle % j == 0:
                divisors += 1
        if divisors > limit:
            print(triangle)
            break


if __name__ == "__main__":
    main(sys.argv[1:])
