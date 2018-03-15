import sys

def birthdayCakeCandles(n, ar):
    x=max(ar)
    print(ar.count(x))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
birthdayCakeCandles(n, ar)
