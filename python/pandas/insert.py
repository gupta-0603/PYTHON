import pandas as pd
var=pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5]})
var.insert(1,"python",var["a"])
var.pop("b")