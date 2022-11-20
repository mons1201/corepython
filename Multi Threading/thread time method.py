import threading

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

display(l)

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

'''import time
l=[1,2,3,4,5,6]
def display(val):
    for x in val:
        time.sleep(4)
        print(x)
display(l)

#

import time
l=[1,2,3,4,5]
def display(val):
    for x in val:
        time.sleep(1)
        print(x)
def display2(val):
    for x in val:
        time.sleep(2)
        print(x)
start=time.time()
display(l)
display2(l)
end=time.time()
print("total time",end-start)

import time

import threading

l=[1,2,3,4,5]
def display(val):
    for x in val:
        time.sleep(1)
        print(x)
def display2(val):
    for x in val:
        time.sleep(2)
        print(x*5)
start=time.time()
t1=threading.Thread(target=display,args=(l,))
t2=threading.Thread(target=display2,args=(l,))
t1.start()
t2.start()
t1.join()
t2.join()

end=time.time()
print("time taken",end-start)'''










