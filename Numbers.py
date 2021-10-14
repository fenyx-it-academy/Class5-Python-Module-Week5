


class Numbers():
    multiplier=2

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+ self.y
   
    def subtract(self,b,c):
        self.b = b
        self.c = c
        return self.b - self.c

    def value(self):
        return (self.x,self.y)

    def multiply(cls,a):
        return cls.multiplier*a

    def value(self):
        return (self.x ,self.y)


numbers = Numbers(3,2)
print(numbers.add())
print(numbers.multiply(3))
print(numbers.subtract(5,2))
print(numbers.value())