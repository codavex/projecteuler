#!/bin/python3

import getopt
import sys


def main(argv):
    limit = 0

    try:
        opts, args = getopt.getopt(argv, "l:", ["limit="])
    except getopt.GetoptError:
        print('0001.py -l <limit>')
        sys.exit()

    # sort out options
    for opt, arg in opts:
        if opt in ("-l", "--limit"):
            limit = int(arg)

    print(SumDivisibleBy(limit, 3) +
          SumDivisibleBy(limit, 5) -
          SumDivisibleBy(limit, 15))


def SumDivisibleBy(limit, n):
    p = int((limit-1) / n)
    return int(n*(p*(p+1)) / 2)


if __name__ == "__main__":
    main(sys.argv[1:])
