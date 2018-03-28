from itertools import product
item_list1= list(map(int, input().strip().split(' ')))
item_list2= list(map(int, input().strip().split(' ')))
result=list((product(item_list1,item_list2)))
for i in result:
    print(i,end=" ")

