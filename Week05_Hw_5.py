'''## Question 5:

* Create a `Vehicle` class with `name`, `max_speed` and `mileage` instance attributes
* Add function `__str__` to vehicle class and print the info about vehicle as: `"Vehicle Model X has max speed 180 and mileage 12"`
* Create a child class `Bus` that will inherit all of the variables and methods of the `Vehicle` class
* Add attribute `capacity` to class `Bus`
* Update `Bus` class such that print message will be: `Bus Breng has max speed 180 and mileage 50 with capacity 100` (**Hint:** Override \__str__ method)
* Add `update_capacity()` method to the class `Bus`
* Create a `Vehicle` and a `Bus` object and print both of them
* call `update_capacity()` method for the earlier created `Bus` object and print it, see the difference'''

class Vehicle:   #Create a `Vehicle` class with `name`, `max_speed` and `mileage` instance attributes
    def __init__(self,name, max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def __str__(self):  #Created a function `__str__` to vehicle class and print the info about vehicle

        return f" Vehicle Model {self.name}  has max speed  {self.max_speed} and mileage {self.mileage}"

class Bus(Vehicle): #Created a child class `Bus` that will inherit all of the variables and methods of the `Vehicle` class,
    
    def __init__(self, name, max_speed, mileage,capacity):  #Added attribute `capacity` to class `Bus`
        super().__init__(name, max_speed, mileage)
        self.capacity=capacity
    
    def __str__(self): 

        return f" Vehicle Model {self.name}  has max speed  {self.max_speed} and mileage {self.mileage} capacity {self.capacity}"
    
    def update_capacity(self,new_capacity): #Added `update_capacity()` method 

        self.capacity=new_capacity
        #return f"Bus Breng has max speed {self.max_speed()} and mileage {self.mileage()} with capacity {self.new_capacity}"


Vehicle1=Vehicle("Mercedes",300,170000) #created a vehicle and bus object and print.
Bus1=Bus("Man",200,450000,40)           #created a vehicle and bus object and print.

print(Vehicle1)
print(Bus1)

Bus1.update_capacity(55)                #updated the capacity with the update_capacity method and print it again.
print(Bus1)