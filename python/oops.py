#classes and objects
class person:
    name='aditya'
    occupation="developer"
    network="10"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
a.name="shubham"  

b.name="riya" # type: ignore
print(a.name)
a.info()
b.info() # type: ignore
