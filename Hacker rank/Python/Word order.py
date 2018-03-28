""""from collections import OrderedDict
N = int(input())
students = []
keys1=[]
for i in range(N):
    students.append(input())
print(students)
list1 = list(set(students))
print(len(list1))
print(students)
for item in students:
    for i in list1
    keys1.append((students.count(item)))
dictionary= dict(zip(keys, [keys1,list2]))
print(abc)"""
"""4
bcdef
abcdefg
bcde
bcdef"""
from collections import OrderedDict
dct = OrderedDict()
for _ in range(int(input())):
    i = input()
    dct[i] = dct.get(i, 0) + 1
print(len(dct))
for w in dct.values():
    print(w, end=' ')