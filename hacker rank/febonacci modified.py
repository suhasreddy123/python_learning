#!/bin/python3

import sys
temp=0

def fibonacciModified(t1, t2, n):
    # Complete this function
    list1=[t1,t2]
    for i in range(0,n):
        temp=t1+t2**2
        t1=t2
        t2=temp
        list1.append(t2)
    print(list1[n-1])

if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    fibonacciModified(t1, t2, n)
