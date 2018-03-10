num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2:
    if num1>num3:
        print("num1 is greater")
    else:
        print("num3 is greater")
elif(num2>num3):
    print("num2 is greater")
else:
    print("num3 is greater")