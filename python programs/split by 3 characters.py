s="iamsuhasreddy"
list=[]
for i in range(0,len(s),2):
    list.append(s[i:i+2])
list=(sorted(list))
print(list)