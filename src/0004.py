#!/bin/python3

import sys


def main(argv):
    largestPalindrome = 0
    for i in range(100, 999):
        for j in range(i, 999):
            product = i * j
            if product > largestPalindrome:
                if str(product) == str(product)[::-1]:
                    largestPalindrome = product

    print(largestPalindrome)


if __name__ == "__main__":
    main(sys.argv[1:])
