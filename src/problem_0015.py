#!/bin/python3

import getopt
import math
import sys


def calculate_routes(value):
    n_factorial = math.factorial(2 * value)
    r_factorial = math.factorial(value)
    n_minus_r_factorial = math.factorial(value)
    return int((n_factorial / r_factorial) / n_minus_r_factorial)


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

    print(calculate_routes(limit))


if __name__ == "__main__":
    main(sys.argv[1:])
