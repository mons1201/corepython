from array import *

var=array('i',[4,2,1,0,6])

def sort(var):
    for i in range(len(var)):
        mini=i
        for j in range(i+1,len(var)):
            if var[mini]>var[j]:
                mini=j
        temp=var[i]
        var[i]=var[mini]
        var[mini]=temp
    print(var)
sort(var)

