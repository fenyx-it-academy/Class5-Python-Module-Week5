class Numbers:
    multiplier = 9

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y

    def multiply(cls,a):
        return cls.multiplier * a

    def subtract(self,b,c):
        self.b = b
        self.c = c
        return self.b - self.c

    def value(self):
        return (self.x, self.y)
    
n = Numbers(3,4)
print(n.add())
print(n.multiply(2))
print(n.subtract(8,4))
print(n.value())