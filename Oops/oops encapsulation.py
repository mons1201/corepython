class Bank:

    def __init__(self):
        self.__value=10 #private value

    def __sam(self): #private value

        print(self.__value)
        print("name:sam")
        print("A/C no:1234")
        print("amount:1000")
        print("address:salem")
        print('\n')
    
    def __ram(self):

        #self.__sam()
        print("name:ram")
        print("A/C no:12345")
        print("amount:8000")
        print("address:covai")

obj=Bank()
obj._Bank__sam()

obj._Bank__ram()


print("values",obj._Bank__value)

        
