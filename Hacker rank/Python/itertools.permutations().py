from itertools import *
item_list= list(( input().strip().split(' ')))
a=item_list[0]
b=int(item_list[1])
result=(list(permutations(a,b)))
list1=[]
for i in result:
    (list1.append("".join(i)))
list1.sort()
for j in list1:
    print(j)