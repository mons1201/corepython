class parent:
    def run(self):
        pass
    
    def start(self):
        self.run()

class child(parent):
    def run(self):
        for i in range(1,11):
            print("hello",i)
c=child()
c.start()