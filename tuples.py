'''a=('sam',1,2,3,4)
print(a)
print(type(a))


#range in tuples
a=('sam','raja','ganesh','anu')
print(a[0:4])
print(a[:2])
print(a[2:])

# if
a=('sam','raja','ganesh','anu')
if 'sam' in a:
    print("welcome")
else:
    print("not valid")


#tuple convert into list
a=('mohana','mons','dinesh','swetha')
b=list(a)
b[2]='sriram'
a=tuple(b)
print(a)

#append method
a=('sam','mons','sriram','swetha')
b=list(a)
b.append("ganesh")
a=tuple(b)
print(a)

#adding tuples in tuple
a=('sam','mons','sriram','swetha')
b=("ganesh",)
a+= b
print(a)

#remove
a=('sam','mons','sriram','swetha')
b=list(a)
b.remove("mons")
a=tuple(b)
print(a)

#joint tuple
a=('sam','mons','sriram','swetha')
b=(14,12,22)
c=a+b
print(c)'''

a=('sam','sathish','pk')
for i in a:
    print(i)
#range methods
a=(1,2,3,'sathish','pk')
for i in range(len(a)):
    print(a[i])
#while loop
a=("sam","raja",1,2,3)
i=0
while i < len(a):
    print(a[i])
    i=i+1