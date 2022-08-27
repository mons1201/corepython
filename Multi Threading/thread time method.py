'''import threading

def display():

    for i in range(1,11):
        print("hai",i)

#display()

t=threading.Thread(target=display)
t.start()

for i in range(1,11):
    print("hello",i)


#time
import time

l=[10,20,30,40,50]

def display(val):
    for x in val:
        time.sleep(1)
        print(x)

display(l)'''

#time calculate

import time

l=[10,20,30,40,50]

def display(val):
    for x in val:
        time.sleep(1)
        print(x)

def display2(val):
    for x in val:
        time.sleep(1)
        print(x)

start=time.time()
display(l)
display2(l)
end=time.time()
print("total timt taken",end-start)








