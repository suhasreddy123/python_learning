# formule for area of triangle is sqrt(s(s-a)(s-b)(s-c)
#s=a+b+c/2
import math
a=float(input())
b=float(input())
c=float(input())
s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)