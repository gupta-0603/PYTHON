import  pandas as pd
l=[1,2,3,4,5,6,7]
var=pd.DataFrame(l)
print(var)
d={"a":[1,2,3,4,5],"s":[1,2,3,4,5]}
var2=pd.DataFrame(d,columns=["a"])
var2.to_csv("test.csv")
