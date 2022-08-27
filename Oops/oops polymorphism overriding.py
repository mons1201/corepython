
#same function name,parameter same

class a:
    def name(self):
        print("ip")
class b(a):
    def name(self):
        super().name()
        print("mohan")
class c(b):
    def name(self):
        super().name()
        print("mani")
x=c()
x.name()