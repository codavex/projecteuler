#!/bin/python3

""" https://projecteuler.net/problem=10 """

import getopt
import sys
import sympy


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

    primes = sympy.primerange(0, limit)
    summation = 0
    for i in primes:
        summation += i

    print(summation)


if __name__ == "__main__":
    main(sys.argv[1:])
