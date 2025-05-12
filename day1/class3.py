


class Employee:
    # constructor is invoked automatically when the object is created
    def __init__(self,name):
        self.name = name  # local variable accessible in all other methods
    def displayEmployee(self):
        print("employee name :", self.name)
    

# object creation
emp1 = Employee('rita')
emp1.displayEmployee()


emp2 = Employee('sita')
emp2.displayEmployee()

emp3 = Employee('gita')
emp3.displayEmployee()