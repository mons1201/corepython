from abc import ABC,abstractmethod

class A(ABC):
    
    @abstractmethod
    def display(self):
        None
        
    @abstractmethod
    def show(self):
        None          
        
class B(A):
    
    def display(self):
        print("hai")
        
    def show(self):
        print("hellow")
        
c=B()
c.display()
c.show()