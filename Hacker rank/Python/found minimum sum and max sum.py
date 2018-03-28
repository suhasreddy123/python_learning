"""Given five positive integers, find the minimum and maximum values that can be calculated by
summing exactly four of the five integers. Then print the respective minimum and maximum values as
a single line of two space-separated long integers."""
#!/bin/python3

import sys

def miniMaxSum(arr):
    #sum=0
    x=sum(arr)
    print(x-max(arr),x-min(arr))




arr = list(map(int, input().strip().split(' ')))
miniMaxSum(arr)
