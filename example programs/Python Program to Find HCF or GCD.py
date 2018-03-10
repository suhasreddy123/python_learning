#Python Program to Find HCF or GCD
num1=int(input())
num2=int(input())
if num1>num2:
    smaller=num2
else:
    smaller=num1
for i in range(1,smaller):
    if num1%i==0 and num2%i==0:
        hcf=i
print(hcf)