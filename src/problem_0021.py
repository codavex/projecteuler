#!/bin/python3

""" https://projecteuler.net/problem=21 """


def get_proper_divisors(num):
    divisors = []
    limit = int(num/2) + 1
    for i in range(1, limit):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    divisor_sums = {}
    for i in range(1, 10000):
        divisor_sums[i] = sum(get_proper_divisors(i))
    summation = 0
    for key, value in divisor_sums.items():
        if value == key:
            continue
        if value in divisor_sums and divisor_sums[value] == key:
            # print(f"{key} {divisor_sums[key]}")
            summation += key
    print(summation)


if __name__ == "__main__":
    main()
