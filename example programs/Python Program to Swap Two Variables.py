#Python Program to Swap Two Variables
a=int(input())
b=int(input())
#method1 using third variable
print("before swap")
print(a)
print(b)
temp=a
a=b
b=temp
print("after swap")
print(a)
print(b)
#method2 with out using third variable
print("after method 2")
a=a+b
b=a-b
a=a-b
print(a)
print(b)