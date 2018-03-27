"""squares = list(map(lambda x: x**2, range(10)))
print(squares)
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
matrix2=[[4,7,9,2],[5,8,4,3],[6,0,1,4]]
print([[row[i] for row in matrix] for i in range(4)])
t={1,3,6,9,3,2,0,2,5,6}
print(t)"""
t=[1,3,6,9,3,2,0,2,5,6]
print(frozenset(t))
print(tuple(t))
print(set(t))
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(set(basket))
basket1 = {'apple':"1", 'orange':"2",'pear':"7",'banana':"5"}
print(basket1)
print(ord("0"))
t=[1,3,6,9,3,2,0,2,5,6]
it=(iter(t))
print(next(it))
a="i am suhas"
#a=(a[::-1])
a=(a.split()[::-1])
print("".join(a))





