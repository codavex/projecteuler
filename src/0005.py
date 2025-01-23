#!/bin/python3

import getopt
import sys


def divByEach(product, limit):
    for i in range(1, limit+1):
        if product % i != 0:
            return False
    return True

def main(argv):
    limit = 20
    primes = [2, 3, 5, 7, 11, 13, 7, 19]  # primes < limit

    product = 1
    for i in range(1, limit+2):
        product = product * i

    for i in primes:
        while divByEach(product/i, limit):
            product = int(product/i)

    print(product)


if __name__ == "__main__":
    main(sys.argv[1:])
