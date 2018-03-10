#Python Program to Find Numbers Divisible by Another Number
my_list=[]
new_list=[]
for i in range(5):
    my_list.append(int(input("enter the list elements :")))
another_number=int(input("enter number :"))
for num in my_list:
    if(num%another_number==0):
        new_list.append(num)
print(new_list)

