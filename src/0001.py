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

    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    print(sum)


if __name__ == "__main__":
    main(sys.argv[1:])
