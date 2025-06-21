# s = {2,4,2,6}
# print(s)
# harry=set()
# t={}
# print(type(harry))
#set methods
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
cities={"tokyo","madrid","berlin","delhi"}
cities2={"seoul","kabul"}
cities3={"tokyo","madrid","delhi"}
print(cities.issuperset(cities3))
print(cities.issubset(cities3))
item=cities.pop()
print(cities)
print(item)