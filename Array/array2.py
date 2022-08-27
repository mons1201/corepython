from array import *

var=array('i',[13,1,7,10,11,4,90])

def first():
    print("finding first minimum,maximum")
    fmin=var[0]
    fmax=var[0]
    smin=var[0]
    smax=var[0]
    for x in var:
        if fmin>x:
            smin=fmin
            fmin=x
        if smin>x and fmin!=x:
            smin=x
        if fmax<x:
            smax=fmax
            fmax=x
        if smax<x and fmax!=x:
            smax=x
    print("first min is: ",fmin)
    print("first max is: ",fmax)
first()