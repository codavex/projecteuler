#!/bin/python3

""" https://projecteuler.net/problem=22 """


def word_value(word):
    summation = 0
    for char in word:
        summation += ord(char) - 64
    return summation


def main():

    summation = 0
    with open("0022_names.txt", encoding="utf-8") as file:
        for line in file:
            names = line.strip().split(",")
            names.sort()
            for i in range(len(names)):
                name = names[i]
                summation += (i + 1) * word_value(name[1:-1])
    print(summation)


if __name__ == "__main__":
    main()
