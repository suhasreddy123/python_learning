"""a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result=[]
if(a0==b0):
    print()
else:
    result.append(1)
if(a1==b1):
    print()
else:
    result.append(1)
if(a2==b2):
    print()
else:
    result.append(1)

print (" ".join(map(str, result)))"""
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result=[]
result1=[]
if(a0==b0):
    print("")
elif(a0>b0):
    result1.append(1)
else:
    result.append(1)
if(a1==b1):
    print("")
elif(a1>b1):
    result1.append(1)
else:
    result.append(1)
if(a2==b2):
    print("")
elif(a2>b2):
    result1.append(1)
else:
    result.append(1)
result.extend(result1)
print (" ".join(map(str, result)))