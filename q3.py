# ## Question 3:

# Create a class called `Numbers`, which has a single class attribute called `multiplier`, and a constructor which takes the parameters `x` and `y` (these should all be numbers).

# * Write a method called `add` which returns the sum of the attributes `x` and `y`.
# * Write a class method called `multiply`, which takes a single number parameter `a` and returns the product of `a` and `multiplier`.
# * Write a method called `subtract`, which takes two number parameters, `b` and `c`, and returns `b - c`.
# * Write a method called `value` which returns a tuple containing the values of `x` and `y`. 
# * Create a numbers object and call all the methods you wrote and print the results.

class Numbers:
    multiplier=1
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    @classmethod
    def change_multiplier(cls,n_multiplier):
        cls.multiplier=n_multiplier
        return cls.multiplier
    @classmethod
    def multiply(cls,a):
        return f'{cls.multiplier} * {a} = {cls.multiplier*a}'
    @staticmethod
    def subtract(b,c):
        return b-c
    def value(self):
        return (self.x,self.y)
numbers=Numbers(5,10)
print(numbers.multiplier)
print(numbers.add())
numbers.multiplier=7
print(numbers.multiplier)
print(numbers.multiply(3)) #1*3 
print(numbers.change_multiplier(7))
print(numbers.multiply(3))
print(numbers.subtract(10,6))
print(numbers.value())
