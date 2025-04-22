#!/bin/python3

""" https://projecteuler.net/problem=27 """

import sympy


def main():
    max_product = -1000 * 1000
    max_consecutive_primes = 0
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            for k in range(0, 1000):
                if not sympy.isprime((k*k) + (i*k) + j):
                    break
            if k > max_consecutive_primes:
                max_consecutive_primes = k
                max_product = i * j
                # print(f"{i} {j} {max_consecutive_primes} {max_product}")

    print(max_product)


if __name__ == "__main__":
    main()
