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

    largestFactor = 0
    factor = 2
    while limit > 1:
        while limit % factor == 0:
            largestFactor = factor
            limit = limit / factor
        factor = factor + 1

    print(largestFactor)


if __name__ == "__main__":
    main(sys.argv[1:])
