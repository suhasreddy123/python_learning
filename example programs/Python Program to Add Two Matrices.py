#Python Program to Add Two Matrices
a=[[1,2,3],
   [2,4,5],
   [7,8,4]]
b=[[87,56,43],
   [23,56,90],
   [21,52,67]]
sum_result=[[0,0,0],
            [0,0,0],
            [0,0,0]]
diff_result=[[0,0,0],
             [0,0,0],
             [0,0,0]]
for x in range(len(a)):
    for j in range(len(a[0])):
        sum_result[x][j]=a[x][j]+b[x][j]
        diff_result[x][j]=b[x][j]-a[x][j]
for r in sum_result:
    print(r)
    #print(diff_result)