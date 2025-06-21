# a=int(input("enter any value between 5 and 9"))

# if(a<5 or a>9):
#     raise ValueError("value should be between 5 and 9 ")
a=input("enter the word")
b=len(a)
if(b<=3):
   a.removeprefix(a[0])
   print(a)
else:
    print(a)  