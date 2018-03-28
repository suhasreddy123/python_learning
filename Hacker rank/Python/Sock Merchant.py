"""9
10 20 20 10 10 30 50 10 20"""
n_of_stocks=int(input())
item_list= list(map(int, input().strip().split(' ')))
itemlist=(item_list.sort())
print(item_list)
from itertools import groupby
iter_elements=[len(list(group)) for key, group in groupby(item_list)]
print(iter_elements)
count=int(0)
for item in iter_elements:
    if item>=2:
        count=int(count)
        count+=item/2
print(int(count))