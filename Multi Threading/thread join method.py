'''
import threading
import time

l=[10,20,30,40,50]

def display(val):
    for x in val:
        time.sleep(1)
        print(x)

def display2(val):
    for x in val:
        time.sleep(1)
        print(x*10)

start=time.time()
t1=threading.Thread(target=display,args=(l,))
t2=threading.Thread(target=display2,args=(l,))
t1.start()
t2.start()
t1.join()  #waiting for next thread
t2.join()
end=time.time()
print("total time taken",end-start)


'''

#join function

import threading
import time

def hotel():
    for i in range(1,6):
        print("preparation",i)
        time.sleep(1)

def hotel2():
    for i in range(1,6):
        print("preparation2",i)
        time.sleep(1)

t1=threading.Thread(target=hotel)
t1.start()
t1.join()
t2=threading.Thread(target=hotel2)
t2.start()
t2.join()

for i in range(1,6):
    print("eating",i)