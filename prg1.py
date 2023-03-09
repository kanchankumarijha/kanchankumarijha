class Employee:
    no_of_leaves=8
   
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"name is {self.name}.salary is {self.salary}.role is {self.role}"
harry=Employee("Harry",30000,"instructor")
rahul=Employee("Rahul",40000,"student")
#harry=Employee()
#rohan=Employee()
#harry.name="harry"
#harry.salary=4000
#harry.age=30

#rohan.name="Rohan"
#rohan.salary=10000
#rohan.age=40
#print(rohan.printdetails())
print(harry.printdetails())


