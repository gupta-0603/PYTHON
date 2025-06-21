# def factorial(n):
#     if(n == 1 or n == 0):
#         return 1
#     else:
#         return(n*factorial(n-1))
    
# n=6   

# print("factorial",factorial(n)) 

def fibonacci(n):
    if(n==0 or n==1):return n
    else:
     return fibonacci(n-1)+fibonacci(n-2)
n=6
print(fibonacci(n))
