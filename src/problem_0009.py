#!/bin/python3

""" https://projecteuler.net/problem=9 """

import math


def main():
    for i in range(1, 1000):
        for j in range(i, 1000):
            k = math.sqrt((i * i) + (j * j))
            if i + j + k == 1000:
                if k * k == (i * i) + (j * j):
                    print(i * j * int(k))


if __name__ == "__main__":
    main()
