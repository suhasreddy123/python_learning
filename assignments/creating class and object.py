file = open("/home/ramesh/Documents/Ramesh.assigment.txt","r")
employeelist=[]
for lines in file:
    employeelist.append(lines.split())
print(employeelist)
file.close()
class employee():
     def __init__ (self,Id,Fname,Lname,Salary,Address_id):
        self.Id=Id
        self.Fname = Fname
        self.Lname = Lname
        self.Salary=int( Salary)
        self.Address_id=Address_id
class address():
    def __init__(self,Address_id ,Plot_no,Streetname, State):
        self.Address_id = Address_id
        self.Plot_no = Plot_no
        self.Streetname = Streetname
        self.State = State

emp1=employee(*employeelist[1])
emp2=employee(*employeelist[2])
emp3=employee(*employeelist[3])
print(emp1.Salary+emp2.Salary+emp3.Salary)
#key=employee.Fname
#fname=[]
#fname.append(emp1.Fname)
#fname.append(emp2.Fname)
#fname.append(emp3.Fname)
#fname.sort()
#print(fname)
#employee(sorted())
#print(emp1.Fname)
import operator
#sorted_x = sorted(employeelist,key=operator.attrgetter('Fname'))
#employeelist.sort(key=operator.attrgetter('Fname'))


