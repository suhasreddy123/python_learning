import math
n=int(input("enter the heigher value of febonacci series:"))
a,b=0,1
#while(b<n):
for x in range(0,n):
    print(b ,end=" ")
    a,b=b,a+b

"""
# Python program to print first n 
# Fibonacci numbers

# Function to print first n 
# Fibonacci Numbers
def printFibonacciNumbers(n):
    f1 = 0
    f2 = 1
    for x in range(0, n):
        print(f2, end=" ")
        f1, f2 = f2, f1 + f2


# Driven code
printFibonacciNumbers(7)"""
