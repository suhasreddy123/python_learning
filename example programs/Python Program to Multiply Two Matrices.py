#Python Program to Multiply Two Matrices
a=[[1,2,3],
   [2,4,5],
   [7,8,4]]
b=[[11,20,13],
   [29,41,50],
   [17,81,47]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            print(i,j,k)
            result[i][j]+=a[i][k]*b[k][j]
for r in result:
    print(r)
