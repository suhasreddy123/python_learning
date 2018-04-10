arr_count = int(input())
arr = list(map(int, input().rstrip().split()))
print(arr)
a=(arr[::-1])
for i in a:
    print(i,end=' ')


