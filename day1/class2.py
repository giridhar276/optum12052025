


class Employee:
    def getEmployee(self,name):
        self.name = name  # local variable accessible in all other methods
    def displayEmployee(self):
        print("employee name :", self.name)
    

# object creation
emp1 = Employee()
emp1.getEmployee('rita')
emp1.displayEmployee()

emp2 = Employee()
emp2.getEmployee('sita')
emp2.displayEmployee()

emp3 = Employee()
emp3.getEmployee('gita')
emp3.displayEmployee()