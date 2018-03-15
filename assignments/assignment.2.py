file = open("/home/ramesh/Documents/Ramesh.assigment.txt","r")
employeelist=[]
for lines in file:
    employeelist.append(lines.split())
print(employeelist)


