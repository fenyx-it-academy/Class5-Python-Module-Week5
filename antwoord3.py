"""Create a class called `Numbers`, which has a single class attribute called 
`multiplier`, and a constructor which takes the parameters `x` and `y` 
(these should all be numbers).

* Write a method called `add` which returns the sum of the attributes
 `x` and `y`.
* Write a class method called `multiply`, which takes a single number 
parameter `a` and returns the product of `a` and `multiplier`.
* Write a method called `subtract`, which takes two number parameters, 
`b` and `c`, and returns `b - c`.
* Write a method called `value` which returns a tuple containing the values
 of `x` and `y`. 
* Create a numbers object and call all the methods you wrote and print the
 results.
 """

class Numbers:
    multiplier = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x+self.y

    @classmethod
    def multiply(cls,a):
        return cls.multiplier * a
    
    def subtract(self,b,c):
        self.b = b
        self.c = c
        return self.b -self.c
    def value(self):
        tulp = (self.x,self.y)
        return tulp
    
obj = Numbers(20,10)
print(obj.add())
print(obj.multiply(5))
print(obj.subtract(13,6))
print(obj.value())