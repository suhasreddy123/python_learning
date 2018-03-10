#Python Program to Print all Prime Numbers in an Interval
lower_limit=int(input())
upper_limit=int(input())
for x in range(lower_limit,upper_limit):
    for i in range(2,x):
        if x%i==0:
            print("",end="")
            break
    else:
        print(x,end=" ")
