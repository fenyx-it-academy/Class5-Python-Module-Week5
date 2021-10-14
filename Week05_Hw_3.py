## Question 3:
'''
Create a class called `Numbers`, which has a single class attribute called `multiplier`, 
and a constructor which takes the parameters `x` and `y` (these should all be numbers).

* Write a method called `add` which returns the sum of the attributes `x` and `y`.
* Write a class method called `multiply`, 
which takes a single number parameter `a` and returns the product of `a` and `multiplier`.
* Write a method called `subtract`, which takes two number parameters, `b` and `c`, and returns `b - c`.
* Write a method called `value` which returns a tuple containing the values of `x` and `y`. 
* Create a numbers object and call all the methods you wrote and print the results.
'''
class Numbers: #Create a class called `Numbers`, which has a single class attribute called `multiplier`,and a constructor which takes the parameters `x` and `y`
    multiplier=1
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self): #a method called `add` which returns the sum of the attributes `x` and `y`.
        return self.x + self.y
    
    def multiply(self,a): #Write a class method called `multiply`,which takes a single number parameter `a` and returns the product of `a` and `multiplier`.

        self.a=a
        return self.a * self.multiplier

    def subtract(self,b,c): #a method called `subtract`, which takes two number parameters, `b` and `c`, and returns `b - c`.
        self.b=b
        self.c=c

        return self.b-self.c
    
    def value(self): #a method called `value` which returns a tuple containing the values of `x` and `y`. 
        tuple=(self.x + self.y)

        return tuple

object=Numbers(6,10) #created a numbers object and call all the methods you wrote and print the results.

print("Add: ",object.add())
print("Multiply:",object.multiply(4))
print("Subtract: ",object.subtract(5,8)) 
print("Numbers: ",object.value())

