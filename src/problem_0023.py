#!/bin/python3

""" https://projecteuler.net/problem=23 """


def get_proper_divisors(num):
    divisors = []
    limit = int(num/2) + 1
    for i in range(1, limit):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    abundant_numbers = []
    for i in range(1, 28124):
        if sum(get_proper_divisors(i)) > i:
            abundant_numbers.append(i)

    sums = []
    for i, abundant_i in enumerate(abundant_numbers):
        for j in range(i, len(abundant_numbers)):
            summation = abundant_i + abundant_numbers[j]
            if summation > 28124:
                break
            if summation not in sums:
                sums.append(summation)

    summation = 0
    for i in range(1, 28124):
        if i not in sums:
            summation += i
    print(summation)


if __name__ == "__main__":
    main()
