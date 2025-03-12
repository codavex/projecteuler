#!/bin/python3

import getopt
import os
import sys


def main(argv):
    testfile = None
    usage = f"{sys.argv[0]} -f <filename>"

    try:
        opts, args = getopt.getopt(argv, "f:", ["filename="])
    except getopt.GetoptError:
        print(usage)
        sys.exit()

    # sort out options
    try:
        for opt, arg in opts:
            if opt in ("-f", "--filename"):
                testfile = arg
        if testfile is None:
            raise ValueError("filename not set")
    except ValueError:
        print(usage)
        sys.exit()

    with open(testfile, encoding="utf-8") as file:
        for line in file:
            command, expected = line.strip().split(",")
            if command[0] == '#':
                continue
            actual = os.popen(command).read().strip()
            if expected == actual:
                print(".", end='', flush=True)
            else:
                print(f"\n{command} - expected {expected} - actual {actual}")
        print("")


if __name__ == "__main__":
    main(sys.argv[1:])
