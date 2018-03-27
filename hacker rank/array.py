data = []
n = int(input())
for i in range(0, n):
    x = (input())
    data.append(x)
    #print(data)
arr2=" ".join(str(item) for item in data)
arr3=" ".join(arr2.split()[::-1])
print(arr3)