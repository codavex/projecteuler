#!/bin/python3

import getopt
import math
import sys


def main(argv):
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = math.sqrt((a * a) + (b * b))
            if a + b + c == 1000:
                if c * c == (a * a) + (b * b):
                    print(a * b * int(c))


if __name__ == "__main__":
    main(sys.argv[1:])
