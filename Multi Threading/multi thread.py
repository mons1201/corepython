#subset of multitask is called multithread

import threading

print(threading.current_thread().getName())

threading.current_thread().setName("abc")
print(threading.current_thread().getName())