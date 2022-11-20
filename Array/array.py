from array import *
'''var=array('i',[1,2,3,4,5,6,7,8,9,0,12])

print(var.buffer_info())  #address and length

print(var.typecode)       #type(int,float)

var.append(26)
print(var)

var.insert(4,14)
print(var)

#reading
print(var[7])
#slicing operator
print(var[:])
print(var[0:2])
print(var[4:10])
print(var[::-1])
print(var[9:2:-1])

#update
var[5]=82
var[0:4]=array('i',[0,0,0])
print(var)

#delete
var.remove(7)
print(var)
var.pop()
print(var)
var.pop(3)
print(var)
del var[4]
print(var)

print(var.count(0))
print(var.itemsize)
print(len(var))
print(var.index(9))'''


#using for loop
'''
var=array('i',[16,2,3,4,5,6,77,88])
def all():
    print("listing the array")
    for x in var:
        print(x,end=" ")

all()'''

var=array('i',[16,2,3,4,5,6,77,88])
def show(index):
    if index<len(var):
        print(var[index],end=" ")
        index+=1
        show(index)

show(2)
