#oops-object oriented programming
#inheritence
#single inheritence        --->one base class one derived class
class father():
    f_name="raja"
    f_age=54
class son(father):
    s_name="bala"
    s_age=18
obj=son()
print("father name:",obj.f_name)
print("son name:",obj.s_name)
print("father age:",obj.f_age)
print("son age:",obj.s_age)


#multiple         ---->two base class and one derived class
class father():
    f_name="raja"
class mother():
    m_name="kavi"
class son(mother,father):
    s_name="bala"
a=son()
print("mother name:",a.m_name)


#multilevel         --->one base class and multiple derived class
class gfather():
    g_father="raja"
class father(gfather):
    f_name="ravi"
class son(father):
    s_name="moha"
class gson(son):
    g_son="mani"
a=gson()
print("gson name:",a.g_son)


#hirerical
class fav:
    def movie(self):
        print("tamil movie")
class b(fav):
    def food(self):
        print("briyani")
class c(fav):
    def game(self):
        print("crkt")
class d(fav):
    def place(self):
        print("dharmapuri")
class f(b,c,d):
    def area(self):
        print("pr patti")
x=f()
x.movie()
x.food()
x.place()
x.game()
x.area()

#another method
class fav:
    def movie(self):
        print("tamil movie")
class b(fav):
    def food(self):
        print("briyani")
class c(fav):
    def game(self):
        print("crkt")
class d(fav):
    def place(self):
        print("dharmapuri")
x=d()
y=c()
z=b()
x.place()
y.game()
z.food()
x.movie()