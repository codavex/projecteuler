#!/bin/python3

import sys


def isPermutation(number):
    strValue = "{:010d}".format(number)
    for char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if char not in strValue:
            return False
    return True


def main(argv):
    lexList = []
    for i in range(123456789, 9876543210):
        if isPermutation(i):
            lexList.append("{:02d}".format(i))
            if len(lexList) > 1000000:
                break

    print(lexList[1000000-1])


if __name__ == "__main__":
    main(sys.argv[1:])
