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

    i = 1
    j = 2
    sum = 0
    while j < limit:
        sum = sum + j
        i, j = j, i+j  # odd
        i, j = j, i+j  # odd
        i, j = j, i+j  # even

    print(sum)


if __name__ == "__main__":
    main(sys.argv[1:])
