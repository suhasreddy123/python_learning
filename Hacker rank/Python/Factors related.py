n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
"""print(a)
print(b)
list_a=[]
list_range=[]
final_list=[]
for i in range(1,(min(b)+1)):
    list_range.append(i)
print(list_range)
list_a=[i for i in list_range if all(i%j==0 for j in a)]
print(list_a)
for i in b:
    for j in list_a:
        if i%j==0:
            final_list.append(j)
print(final_list)"""
ct=0
for i in range(max(a),min(b)+1):
    for j in a:
        if i%j!=0:
            break
    else:
        for k in b:
            if k%i!=0:
                break
        else:
            ct+=1
print (ct)








