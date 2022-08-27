
'''class con1:
    def __init__(self):
        print("Nothing More Then happiness")

    def hello(self):
        print("happiness")

c1=con1()
c1.hello()



#constrator using parameter
class con:
    def __init__(self,name,age,college):
        print("name:",name)
        print("age:",age)
        print("college:",college)

c=con("mohan",25,"MEC")    #parameter passing

#accessing constrator object in normal function using self keyword

class comp:
    def __init__(self,place,company):
        self.a=place
        self.b=company

    def fun(self):
        print("place:",self.a)
        print("company:",self.b)
    
c=comp("chennai","CTS")
c.fun()
'''

#addition programme

class a:
    def __init__(self,b,c):
        self.b=b
        self.c=c
    
    def add(self):
        d=self.b+self.c
        print("add",d)

a1=a(10,20)
a1.add()
