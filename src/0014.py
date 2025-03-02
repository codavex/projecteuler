#!/bin/python3

import getopt
import sys


def main(argv):
    limit = None
    usage = f"{sys.argv[0]} -l <limit>"

    try:
        opts, args = getopt.getopt(argv, "l:", ["limit="])
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

    maxChain = 0
    maxStartingValue = 0
    for i in range(1, limit):
        test = i
        chain = 1
        while test != 1:
            chain += 1
            if test % 2 == 0:
                test = int(test / 2)
            else:
                test = (3 * test) + 1
        if chain > maxChain:
            maxChain = chain
            maxStartingValue = i

    print(maxStartingValue)


if __name__ == "__main__":
    main(sys.argv[1:])
