#!/bin/python3

import getopt
import sys


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

    summation = int(limit * (limit + 1) / 2)
    sumOfSquares = int(((2*limit) + 1)*(limit + 1)*limit/6)
    print((summation*summation) - sumOfSquares)


if __name__ == "__main__":
    main(sys.argv[1:])
