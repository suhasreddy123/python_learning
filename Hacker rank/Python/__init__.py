def getMoneySpent(keyboards, drives, s):
    c = []
    new_list=[]
    for i in keyboards:
        for j in drives:
            k = i + j
            c.append(k)

    if s<=max(c):
        print(max(c))

    else:
        print("-1")

s, n, m = input().strip().split(' ')
s, n, m = [int(s), int(n), int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
getMoneySpent(keyboards, drives, s)
