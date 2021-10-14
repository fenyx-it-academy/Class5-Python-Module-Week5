"""Create a class called Numbers, which has a single class attribute called multiplier, and a constructor which takes the parameters x and y (these should all be numbers).

Write a method called add which returns the sum of the attributes x and y.
Write a class method called multiply, which takes a single number parameter a and returns the product of a and multiplier.
Write a method called subtract, which takes two number parameters, b and c, and returns b - c.
Write a method called value which returns a tuple containing the values of x and y.
Create a numbers object and call all the methods you wrote and print the results."""


class Numbers:
    multiplier = 1.5         #we assign class attribute as 1.5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):           #returns the sum of the attributes x and y.
        return self.x + self.y

    def multiply(self, m):   #returns multiply m by class attribute(1.5)
        return self.multiplier* m

    def value(self):         #converts x,y to tuple(x,y)
        return (self.x,self.y)

    def subtract(self,b, c): #we assign new parameters,these take another values than x,y.
        self.b=b
        self.c=c
        return b - c
#m,b,c are not assigned at __init_  intentionally.
numbers=Numbers(5,10)
print("The sum of the attributes x and y: %d"%(numbers.add()))
print("The substract : %d"%numbers.subtract(2,3))
print("The multiplied by (1.5): %d"%numbers.multiply(2))
print(numbers.value())

