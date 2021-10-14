"""
  Create a `Vehicle` class with `name`, `max_speed` and `mileage` instance attributes
* Add function `__str__` to vehicle class and print the info about vehicle as: `"Vehicle Model X has max speed 180 and mileage 12"`
* Create a child class `Bus` that will inherit all of the variables and methods of the `Vehicle` class
* Add attribute `capacity` to class `Bus`
* Update `Bus` class such that print message will be: `Bus Breng has max speed 180 and mileage 50 with capacity 100`
 (**Hint:** Override \__str__ method)
* Add `update_capacity()` method to the class `Bus`
* Create a `Vehicle` and a `Bus` object and print both of them
* call `update_capacity()` method for the earlier created `Bus` object and print it, see the difference"""

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self):
        return f"Vehicle {self.name} has max speed {self.max_speed} and mileage {self.mileage}"
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage,capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity
    def __str__(self):
        return super().__str__() + (f" with capacity {self.capacity}")
    def update_capacity(self,capacity):
        self.capacity = capacity
car1 = Vehicle("toyota",150,2500)
print(car1)
bus1 = Bus("mercedes",180,200000,100)
print(bus1)
bus1.update_capacity(150)
print(bus1)