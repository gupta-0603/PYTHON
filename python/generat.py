def my_generator():
    for i in range(5):
        yield i
gen=my_generator()
print(next(gen))        
 #       used when you want to run separtely the program like for only two ntime in loop of 1000