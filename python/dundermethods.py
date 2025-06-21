class employee:
    name="harry"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
            return 1

e=employee()
print(e.name)    