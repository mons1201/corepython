'''#AttributeError
try:
    class a:
        
        pass
    A=a()
    a.hello()
    
except AttributeError as e:
    print("attribute error",e)
    
    
#name error
try:
    name="mohan"
    print(age)
    
except NameError as e:
    print("name error",e)
    
#value error
try:
    n=int(input("enter the number"))
    print(n)
    
except ValueError as e:
    print("value error",e)
    
#key error
try:
    aa={"name":"mohan","name2":"mani"}
    print(aa['age'])
except KeyError as e:
    print("key error",e)
    
#index error
try:
    li=[1,2,3,4]
    print(li[5])
except IndexError as e:
    print("index error",e)
    
#exception
try:
    a=10
    b=0
    c=a/b
    print(c)
    
except Exception as e:
    print(e)
    '''
#how many error accur in python

err=dir (locals()['__builtins__'])
print(err)
print(len(err))