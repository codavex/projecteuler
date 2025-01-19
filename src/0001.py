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

    print(SumDivisibleBy(limit, 3) +
          SumDivisibleBy(limit, 5) -
          SumDivisibleBy(limit, 15))


def SumDivisibleBy(limit, n):
    p = int((limit-1) / n)
    return int(n*(p*(p+1)) / 2)


if __name__ == "__main__":
    main(sys.argv[1:])
