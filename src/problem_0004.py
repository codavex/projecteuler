#!/bin/python3

""" https://projecteuler.net/problem=4 """


def main():
    largest_palindrome = 0
    for i in range(100, 999):
        for j in range(i, 999):
            product = i * j
            if product > largest_palindrome:
                if str(product) == str(product)[::-1]:
                    largest_palindrome = product

    print(largest_palindrome)


if __name__ == "__main__":
    main()
