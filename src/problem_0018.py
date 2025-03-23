#!/bin/python3

""" https://projecteuler.net/problem=16 """

import getopt
import sys


def read_array(filename):
    array = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            numbers = line.strip().split(" ")
            inner_array = []
            for num in numbers:
                inner_array.append(int(num))
            array.append(inner_array)
    return array


def main(argv):
    filename = None
    usage = f"{sys.argv[0]} -f <filename>"

    try:
        opts, _ = getopt.getopt(argv, "f:", ["filename="])
    except getopt.GetoptError:
        print(usage)
        sys.exit()

    # sort out options
    try:
        for opt, arg in opts:
            if opt in ("-f", "--filename"):
                filename = arg
        if filename is None:
            raise ValueError("filename not set")
    except ValueError:
        print(usage)
        sys.exit()

    test_array = read_array(filename)

    depth = len(test_array)
    for i in range(1, depth):
        for j in range(len(test_array[i])):
            # print(f"{i} {j}")
            # print(test_array[i-1])
            # print(test_array[i])
            focus = test_array[i][j]
            above_left = 0
            if j != 0:
                above_left = test_array[i-1][j-1]
            above_right = 0
            if j < len(test_array[i]) - 1:
                above_right = test_array[i-1][j]
            # print(f"{focus} {above_left} {above_right}")
            test_array[i][j] = max(focus+above_left, focus+above_right)
        # print("")

    max_path = 0
    for i in test_array[-1]:
        if i > max_path:
            max_path = i
    print(max_path)


if __name__ == "__main__":
    main(sys.argv[1:])
