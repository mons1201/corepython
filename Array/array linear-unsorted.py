#linear-->unsorted

from array import *

var=array('d',[1.2,4.5,3.2,5.7,2.4,5.7,6.8]) #d or f

def linear(data):
    print(data,"searched by linear way")
    for index in range(len(var)):
        if var[index]==data:
            return index
    else:return -1

users=float(input("Tell us data want to search: "))
pos=linear(users)

if pos!=-1:print(users,"found @",pos)
else:print(users,"not found anywhere")