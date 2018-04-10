n_of_stocks=int(input())
a= set(list(map(int,str(input()).strip().split(' '))))
n_of_stocks2=int(input())
b= set(list(map(int, str(input()).strip().split(' '))))
a1=[]
a1=list(a.difference(b))
b1=list(b.difference(a))
a1.extend(b1)
a1.sort()
for i in a1:
    print(i)