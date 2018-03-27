#Python Program to Print the Fibonacci sequence
"""num=int(input())
a,b=0,1
while(b<=num):
    print(a, end=" ")
    a,b=b,a+b
    #print(b,end=" ")"""
# print first n febonacci numbers
#num=int(input())
"""a,b,count=0,1,0
while( count<=5):
    print(b, end=" ")
    count=count+1
    a,b=b,a+b
    #print(b,end=" ")
n=int(input())
a,b=0,1
while(b<=n):
    #print(a, end=" ")
    a,b=b,a+b
    print(b,end=" ")"""
"""import math
x=1
b=2
r=(math.sqrt(5))
#a=math.cos(1/r)
#b=math.sin(2/r)
c=math.atan(2)
print(r)
print(c)
2.23606797749979
1.1071487177940904"""
import cmath
a=1+2j
#print(int(a))
b=(cmath.polar(a))
for i in range(len(b)):
    print(b[i])
complex(input())