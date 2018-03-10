#Python Program to Find the Sum of Natural Numbers
n=int(input())
sum1=(n*(n+1))/2
print(sum1)
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)