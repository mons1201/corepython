'''from multiprocessing import Lock
import threading
import time

def display(name):
    print("hi",end=" ")
    time.sleep(1)
    print(name)

name1="raja"
name2="rani"
t1=threading.Thread(target=display,args=(name1,))
t2=threading.Thread(target=display,args=(name2,))
t1.start()
t2.start()'''

#lock function

from multiprocessing import Lock
import threading
import time

l=Lock()
def account(name):
    l.acquire()  #thread acquires this lock
    print("hi",end=" ")
    time.sleep(1)
    print(name,"is deposite to the account now")
    l.release()  #thread releases this lock

name1="raja"
name2="rani"
t1=threading.Thread(target=account,args=(name1,))
t2=threading.Thread(target=account,args=(name2,))
t1.start()
t2.start()

