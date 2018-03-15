strg="i am suhas"
str=strg.split()
n=len(str)
print(str)

for i in range (0,n):
    a=((str[i][::-1]))
    print(a,end=" ")