#!/bin/python3

import getopt
import sympy
import sys


def divByEach(product, limit):
    for i in range(1, limit+1):
        if product % i != 0:
            return False
    return True

def main(argv):
    limit = None
    helpString = f"{sys.argv[0]} -l <limit>"

    try:
        opts, args = getopt.getopt(argv, "l:", ["limit="])
    except getopt.GetoptError:
        print(helpString)
        sys.exit()

    # sort out options
    try:
        for opt, arg in opts:
            if opt in ("-l", "--limit"):
                limit = int(arg)
        if limit is None:
            raise ValueError("Limit not set")
    except ValueError:
        print(helpString)
        sys.exit()

    primes = sympy.primerange(0, limit)
    product = 1
    for i in range(1, limit+1):
        product = product * i

    for i in primes:
        while divByEach(product/i, limit):
            product = int(product/i)

    print(product)


if __name__ == "__main__":
    main(sys.argv[1:])
