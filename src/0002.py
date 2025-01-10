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
    sum = 2
    while True:
        next_in_series = i + j
        i = j
        j = next_in_series
        if j > limit:
            break
        if j % 2 == 0:
            sum = sum + j

    print(sum)


if __name__ == "__main__":
    main(sys.argv[1:])
