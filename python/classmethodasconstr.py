class employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary=12000
@classmethod
def from_string(cls,string):
    name,age=string.split(",")
    return cls(name,int(age))
e=employee("harry",12000)
print(e.name,e.salary) 
string="harry-12"    
e=employee(string.split("-"),12)