import threading
import time

def job():
  str1="Sub thread:"
  str2=""
  for i in range(1,5):
    str2=str1+str(i)+"\n"  
    print(str2)  
    time.sleep(1)

st = threading.Thread(target = job)
st.start()

str1="Main thread:"
str2=""
for i in range(1,3):
   str2=str1+str(i)+'\n' 
   print(str2)
   time.sleep(1)

print("finish")




