#!/bin/python3

""" https://projecteuler.net/problem=20 """

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

    product = 1
    for i in range(1, limit + 1):
        product = product * i

    product_string = str(product)

    total = 0
    for char in product_string:
        total += int(char)

    print(total)


if __name__ == "__main__":
    main(sys.argv[1:])
