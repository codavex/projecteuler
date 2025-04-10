#!/bin/python3

""" https://projecteuler.net/problem=24 """


def is_permutation(number):
    str_value = "{:010d}".format(number)
    for char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if char not in str_value:
            return False
    return True


def main():
    lex_list = []
    for i in range(123456789, 9876543210):
        if is_permutation(i):
            lex_list.append("{:02d}".format(i))
            if len(lex_list) > 1000000:
                break

    print(lex_list[1000000-1])


if __name__ == "__main__":
    main()
