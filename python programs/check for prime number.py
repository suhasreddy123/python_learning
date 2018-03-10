"""for n in range(2, 1000):
    for x in range(2, n):
       if n % x == 0:
           #print(n, 'equals', x, '*', n//x)
           break
    else:
            print(n,end=",")"""
import math
n=int(input())
for i in range (2,n):
    for x in range(2,i):
        if i%x==0:
            print(i,"not prime")
            break
    else:
        print(i,"is prime")
"""n1=int(n**0.5)
for i in range (2,n):n
    for x in range (2,n1):
        if i % x == 0:
           #print(i, "not prime")
        break
    else:
        print(i,end=' ')"""


