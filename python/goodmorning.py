import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)

if(hour>0 and hour<12):
 print("good morning")
elif(hour>12 and hour<17):
  print("good afternoon")
if(hour>17 and  hour<0):
    print("good night sir")  
    a=5
    b=4
if(hour>0):
       print("yes")