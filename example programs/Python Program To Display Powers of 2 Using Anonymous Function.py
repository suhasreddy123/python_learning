#Python Program To Display Powers of 2 Using Anonymous Function
def power(num):
    n = int(input("enter powers range"))
    for i in range(1,n+1):
        result=num**i
        print("2 power",i,result)

power(2);
a=lambda x:x**2
print(a(3))

