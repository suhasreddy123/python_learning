"""def multipliers ():
    return [lambda x: i * x for i in range (4)]
print ([m (2) for m in multipliers ()])
import time
print (time.localtime());"""
"""n=int(input())
for i in range(2,n):
    for j in range(2,i):
        if(i%j==0):
          break
    else:
        print("it is prime:",i)"""

"""n=int(input())
for i in range(2,n):
    if(n%i==0):
        print("it is not prime number")
        break
else:
    print("is a prime number",n)"""
lower=int(input())
upper=int(input())

for num in range(lower,upper+1):
    order = len(str(num))
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print("num is armstrong number",num)






