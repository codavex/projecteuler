#!/bin/python3

import getopt
import sys
import sympy


def div_by_each(product, limit):
    for i in range(1, limit+1):
        if product % i != 0:
            return False
    return True


def main(argv):
    limit = None
    usage = f"{sys.argv[0]} -l <limit>"

    try:
        opts, args = getopt.getopt(argv, "l:", ["limit="])
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
    product = 1
    for i in range(1, limit+1):
        product = product * i

    for i in primes:
        while div_by_each(product/i, limit):
            product = int(product/i)

    print(product)


if __name__ == "__main__":
    main(sys.argv[1:])
