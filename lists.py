'''from cgi import print_arguments


prob=['mohan',5,6,7,8,'m']
print(prob)
#adding elements in end if list
prob.append('goodluck')
print(prob)
print(len(prob))
print(prob)

#adding new elements in list
prob.insert(5,8)
print(prob)

#replace the data in respective position
prob[6]= 'angel'
print(prob)

#adding values in list
total=[10,100,1000,10000,100000]
print(min(total))

#sum of list
print(sum(total))

#remove and pop the list operation
total.remove(100000)
print(total)
print(total.pop())
print(total.pop(1))
print(total)
print(total.reverse())
print(total)

#list copy method
l=[1,2,3,4,5,6,7]
a=l.copy()
print('copy:',a)
count=a.count(5)
print(count)

n=int(input("enter the list:"))
list1=[]
for i in range(n):
    lival=input("enter the list:")
    list1.append(lival)
    print("list:",list1)

#insert
a=[12,13,14,15,15]
print("original list:",a)
val=int(input("enter the new elements:"))
insert=int(input("enter the position:"))
a.insert(insert,val)
print("added list:",a)'''

#split
a=input("enter the name")
list=a.split(",")
for i in list:
    print(i)
