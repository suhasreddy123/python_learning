#!/bin/python3

import sys


def plusMinus(arr):
    count_neg = 0
    count_zero = 0
    count_pos = 0
    for item in arr:
        if item < 0:
            count_neg = count_neg + 1
        elif item > 0:
            count_pos = count_pos + 1
        else:
            count_zero = count_zero + 1
    print(count_neg)
    print(count_pos)
    print(count_zero)

    print('{0:.6f}'.format(count_neg /n))
    print('{0:.6f}'.format(count_pos / n))
    print('{0:.6f}'.format(count_zero / n))

    # Complete this function


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
