import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
var["C"]=var["A"]+var["B"]
print(var  )