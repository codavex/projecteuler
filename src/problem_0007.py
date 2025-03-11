#!/bin/python3

import getopt
import sys


def main(argv):
    limit = None
    usage = f"{sys.argv[0]} -l <limit>"

    try:
        opts, _ = getopt.getopt(argv, "l:", ["limit="])
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

    primes = [2]
    test = 1
    while len(primes) < limit:
        test += 2
        if is_prime(test, primes):
            primes.append(test)

    print(primes[-1])


def is_prime(test, primes):
    for i in primes:
        if test % i == 0:
            return False
    return True


if __name__ == "__main__":
    main(sys.argv[1:])
