import math
n=5
a,b=0,1
s=[a,b]
k=[]

while(b<=n-3):
    a,b=b,a+b
    s.append(b)
for item in s:
    p=pow(item,3)
    k.append(p)
print(k)
    # complete the lambda function
    # return a list of fibonacci numbers
