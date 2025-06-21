# def average(a,b):
#     print("the average is", (a+b)/2)

# average(4, 6)    

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
        print("the average is:", sum/len(numbers))
  
  
print("hello")                