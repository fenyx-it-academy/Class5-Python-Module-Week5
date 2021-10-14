"""Create a class called `Numbers`, which has a single class attribute called `multiplier`,
 and a constructor which takes the parameters `x` and `y` (these should all be numbers).

* Write a method called `add` which returns the sum of the attributes `x` and `y`.
* Write a class method called `multiply`, which takes a single number parameter `a` and returns the product of `a` and `
multiplier`.
* Write a method called `subtract`, which takes two number parameters, `b` and `c`, and returns `b - c`.
* Write a method called `value` which returns a tuple containing the values of `x` and `y`. 
* Create a numbers object and call all the methods you wrote and print the results."""

class Numbers:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x +self.y
    def multiply (self,a,multiplier):
        self.multiplier = multiplier
        return a * self.multiplier
    def subtract(self,b,c):
        return b-c
    def value(self):
        return (self.x, self.y)
number = Numbers(10,15)
print(number.add())
print(number.multiply(10,15))
print(number.subtract(10,5))
print(number.value())