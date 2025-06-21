x=[3,4,5,6,7]
var=pd.Series(x,index=['a','s','d','f','t'])
print(var)
print(var[2])
dic={"name":['python','c','c++','java'],"por": [12,13,14,15],"rank":[1,4,3,2]}
var1=pd.Series(dic)
print(var1)