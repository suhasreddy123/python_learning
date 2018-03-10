#Python Program to Check Prime Number
"""num=int(input())
for i in range(2,num):
    for x in range(2,i):
        if i%x==0:
            print("it is not prime")
            break
    else:
        print("it is prime")"""
"""num=int(input())
for x in range(2,num):
    if num%x==0:
        print(num,"not prime")
        break
else:
    print(num,"is a prime")"""
#first n prime numbers
"""num=int(input())
list=[]
count=0
for i in range(2,num):
    for x in range(2,i):
        if i%x==0:
            print("",end="")
            break
    else:
        list.append(i)
print(list[:10])"""
#print prime numbers in range:
lower_limt=int(input())
upper_limit=int(input())
for i in range(lower_limt,upper_limit):
    for x in range(2,i):
        if i%x==0:
            print("",end="")
            break
    else:
        print(i,end=" ")
