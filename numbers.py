class Numbers:
        def __init__(self,x,y):
                self.x=x
                self.y=y
                
        def add(self):
                print(self.x+self.y)

        def multiply(self,a,multiplier):
                self.multiplier=multiplier
                print(a*self.multiplier) 
        def substract(self,b,c):
                print(b-c)
        def value(self):
                k=(self.x,self.y)
                print(k)

Number=Numbers(8,9)
Number.add()
Number.multiply(7,6)
Number.substract(3,1)
Number.value()


