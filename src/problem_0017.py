#!/bin/python3

import getopt
import sys


units_words = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
tens_words = {
    0: "",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}
teens_words = {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}


def convert_to_words(i):
    retStr = ""
    if i > 1000:
        return "too big"
    if i == 1000:
        return "onethousand"
    hundreds = int(i/100)
    # print(hundreds)
    if hundreds > 0:
        retStr += units_words[hundreds]
        retStr += "hundred"
    under_hundreds = i % 100
    # print(under_hundreds)
    if hundreds > 0 and under_hundreds > 0:
        retStr += "and"
    tens = int(under_hundreds/10)
    units = under_hundreds % 10
    # print(f"{tens} {units}")
    if tens == 1:
        retStr += teens_words[units]
    else:
        retStr += tens_words[tens]
        retStr += units_words[units]
    # print(f"{i} {retStr} {len(retStr)}")
    return retStr


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

    summation = 0
    for i in range(1, limit+1):
        summation += len(convert_to_words(i))
    print(summation)


if __name__ == "__main__":
    main(sys.argv[1:])
