#!/bin/python3

import sys

def diagonalDifference(a):
    sum_first_diagonal = sum(a[i][i] for i in range(n))
    sum_second_diagonal = sum(a[i][n-i-1] for i in range(n))
    result=abs(sum_first_diagonal-sum_second_diagonal)
    return result

n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)
result = diagonalDifference(a)
print(result)