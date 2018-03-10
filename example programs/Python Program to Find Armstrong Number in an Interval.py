#Python Program to Find Armstrong Number in an Interval
lower_interval=1
upper_interval=1000

for i in range(lower_interval,upper_interval,1):
    sum=0
    digit=len(str(i))
    temp=i
    while(temp>0):
        no=temp%10
        sum=sum+(no**digit)
        temp//=10
    if(i==sum):
        print(i,end=" ")
