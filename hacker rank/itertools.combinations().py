from itertools import *
item_list= list(( input().strip().split(' ')))
a=item_list[0]
b=int(item_list[1])
list1=[]
list2=[]
for item in range(len(a)):
    list2.append(a[item])
list2.sort()
result=(list(combinations_with_replacement(list2,b)))
for j in result:
    print("".join(j))
