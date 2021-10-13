class Numbers:#I created a class called Numbers, which has a single class attribute called multiplier, 
              #and a constructor which takes the parameters x and y
    multiplier=2
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def add(self):#I wrote a method called add which returns the sum of the attributes x and y.
        return self.x + self.y

    def multiply(self,a):# I wrote a class method called multiply, which takes 
                          #a single number parameter a and returns the product of a and multiplier.
        self.a=a
        return self.a*Numbers.multiplier

    def subtract(self,b,c):# I wrote a method called subtract, which takes two number parameters, b and c, and returns b - c.
        self.b=b
        self.c=c
        return self.b - self.c
    
    def value(self):#I wrote a method called value which returns a tuple containing the values of x and y.
        tuple=(self.x,self.y)
        
        return tuple

obj=Numbers(1,2) #I created a numbers object and call all the methods you wrote and print the results.
print("Numbers: ",obj.value())
print("Add: ",obj.add())
print("Multiply:",obj.multiply(3))
print("Subtract: ",obj.subtract(1,2))