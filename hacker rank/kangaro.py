#!/bin/python3

import sys

#def kangaroo(x1, v1, x2, v2):
    # Complete this function

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
#result = kangaroo(x1, v1, x2, v2)
#print(result)
n=10
n1=[]
n2=[]
is_match = "NO"
for i in range (0,n):
    i_d=x1+(v1*i)
    j_d = x2 + (v2 * i)
    if (i_d == j_d):
        print("YES")
        break
print(is_match)

