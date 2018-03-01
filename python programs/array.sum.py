"""data = []
n = int(input())
for i in range(0, n):
    x = (input(),end=" ")
sum1=sum(data)
print(sum1)
    #print(data)
arr2=" ".join(str(item) for item in data)
arr3=" ".join(arr2.split()[::-1])
print(arr3)"""
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
print(sum(ar))