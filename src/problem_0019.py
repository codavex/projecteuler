#!/bin/python3

""" https://projecteuler.net/problem=19 """

import sys


def main(argv):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    sundays = 0
    day = 1 + 365  # call Monday 1, plus 1900 number of days
    for year in range(1901, 2001):
        for i in months:
            if day % 7 == 0:  # if Monday is 1, Sunday is 0
                sundays += 1
            day = day + months[0]
            if months == 1 and year % 4 == 0:
                # doesn't deal with centuries, but we don't need
                day += 1

    print(sundays)


if __name__ == "__main__":
    main(sys.argv[1:])
