num=50
#print(max(map(len, bin(num)[2:].split('0'))))
a=(bin(num)[2:])
b=a.split('0')
print(max(map(len,b)))