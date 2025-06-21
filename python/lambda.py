def appl(fx,value):
    return 6+fx(value)


double=lambda x: x*x
cube= lambda x: x*x*x
avg=lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(4))
print(avg(3,5,10))
print(appl(cube,2))

  