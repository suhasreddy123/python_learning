#Python Program to Transpose a Matrix
a=[[1,2,3],
   [2,4,5],
   [7,8,4]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j]=a[j][i]
for r in result:
    print(r)