a_list=["atm1","atm2","atm3","atm4","atm5","atm6","atm7","atm8","atm9","atm10","atm11"]
#reverse list
a_list=a_list[::-1]
n=int(input("enter number of elements in a split:"))
a_list=[a_list[i:i+n] for i in range(0, len(a_list), n)]
#reverse list
a_list=a_list[::-1]
print(a_list)
result=[]
for i in range (len(a_list)):
    result.append((a_list[i]))
