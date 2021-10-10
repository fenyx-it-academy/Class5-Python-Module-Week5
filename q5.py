# ## Question 5:

# * Create a `Vehicle` class with `name`, `max_speed` and `mileage` instance attributes
# * Add function `__str__` to vehicle class and print the info about vehicle as: `"Vehicle Model X has max speed 180 and mileage 12"`
# * Create a child class `Bus` that will inherit all of the variables and methods of the `Vehicle` class
# * Add attribute `capacity` to class `Bus`
# * Update `Bus` class such that print message will be: `Bus Breng has max speed 180 and mileage 50 with capacity 100` (**Hint:** Override \__str__ method)
# * Add `update_capacity()` method to the class `Bus`
# * Create a `Vehicle` and a `Bus` object and print both of them
# * call `update_capacity()` method for the earlier created `Bus` object and print it, see the difference

class Vehicle:
    def __init__(self,name,max_speed,millage):
        self.name=name
        self.max_speed=max_speed
        self.millage=millage
    def __str__(self):
        return f'Vehicle Model {self.name} has max speed {self.max_speed} and millage {self.millage}'
class Bus(Vehicle):
    def __init__(self, name, max_speed, millage,capacity):
        super().__init__(name, max_speed, millage)
        self.capacity=capacity
    def __str__(self):
        return f'Bus {self.name} has max speed {self.max_speed} and millage {self.millage} with capacity {self.capacity}'
    def update_capacity(self,update):
        self.capacity=update
ve1=Vehicle('Veh X',220,10)
bus1=Bus('Bus X',180,12,45)
print(ve1)
print(bus1)
bus1.update_capacity(50)
print(bus1)