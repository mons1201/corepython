#Binary--> sorted

from array import *

house=array('i',[3,4,6,9,24,35,67,89,90,135,250,1250])

def binary(data,start=0,end=len(house)-1):
    if start<=end:
        mid=int((start+end) / 2)
        if house[mid] == data:return mid
        elif house[mid] >data:return binary (data, start,mid)
        else:return binary(data,mid+1,end)
    else:
        return 0

users=int(input("Tell us data want to search: "))
pos=binary(users)
if pos!=0:print(users,"found @",pos)
else:print(users,"not found anywhere")

