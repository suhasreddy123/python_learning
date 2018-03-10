#Python Program to Make a Simple Calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation")
print("1.add")
print("2.sub")
print("3.mult")
print("4.divide")
choise=input("enter choice 1/2/3/4 : ")
n1=int(input("enter 1 st number"))
n2=int(input("enter 2 nd number"))
if choise=="1":
    print(add(n1,n2))
elif choise=="2":
    print(sub(n1,n2))
elif choise=="3":
    print(mult(n1,n2))
elif choise=="4":
    print(divide(n1,n2))
else:
    print("enter a valid input")
