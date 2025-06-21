f=open('new1.txt' ,'w')
f.write('hello world')
f.close()
with open('new1.txt','a') as f:
       
    f.write("hello")
# text=f.read()
# print(text)

# f.close()


