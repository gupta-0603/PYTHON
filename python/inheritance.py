class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")
#inheritance
class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2= Employee("mohan",420)
e2.showDetails()