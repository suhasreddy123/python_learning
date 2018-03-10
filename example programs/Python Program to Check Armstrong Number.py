num=int(input())
sum=0
pow=len(str(num))
temp=num
while(temp>0):
    digit=temp%10
    sum=sum+(digit**pow)
    temp//=10
if num==sum:
    print("num is armstrong number")
else:
    print("not a armstrong number")
