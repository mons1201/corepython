'''def A():
    print("hai")
A()


def add():
    a=10
    b=10
    c=a+b
    print(c)
add()
#parameter passing funtiom
def b(age):
    print(age)
b(25)

def c(degree):
    print(degree)
c("EEE")


#
def fun():
    a=input("enter the degree:")
    b=float(input("enter the percentage:"))
    if(a=='B.E' and b>=70):
        print("1st class")
    elif(a=='B.E' and b<=60):
        print("2nd class")
    else:
        print("not eligible")
fun()


def vote(name,age,location):
    if age==18:
        print(name,"is eligible for voteing",location)
    elif age==21:
        print(name,"is eligible for voteing",location)
    else:
        print("you are not eligible for voteing")
vote("mohaana",18,"salem")
vote("mons",20,"covai")

#change the oredr means using key
vote(age=25,location="madurai",name="mm")'''



#skill

def fun():
    a=input("enter the skill:")
    b=float(input("enter yor experience:"))
    if(a==("java" or "python") and b>=2 and b<=5):
        print("team leader")
    elif(a==("java" or "python") and b>=6 and b<=10):
        print("manager")
    else:
        print("not eligible")
fun()