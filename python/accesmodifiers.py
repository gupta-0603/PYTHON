class employee:
    def __init__(self):
        self.name="harry"

a=employee()
print(a.name)
#now we cant access name 
class employee:
    def __init__(self):
        self.__name="harry"

a=employee()
# print(a.name)
#to acess use this
print(a._employee__name)