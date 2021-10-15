"""Create a Vehicle class with name, max_speed and mileage instance attributes
Add function __str__ to vehicle class and print the info about vehicle as: "Vehicle Model X has max speed 180 and mileage 12"
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
Add attribute capacity to class Bus
Update Bus class such that print message will be: Bus Breng has max speed 180 and mileage 50 with capacity 100 (Hint: Override _str_ method)
Add update_capacity() method to the class Bus
Create a Vehicle and a Bus object and print both of them
call update_capacity() method for the earlier created Bus object and print it, see the difference
"""
class Vehicle:
    
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f'Vehicle Model {self.name} has max speed {self.max_speed} and mileage {self.mileage}'

class Bus(Vehicle):

    def __init__(self,name,max_speed,mileage,capacity):
        self.capacity = capacity
        super().__init__(name,max_speed,mileage)

    def __str__(self):
        return f'Bus Breng has max speed {self.max_speed} and mileage {self.mileage} with capacity {self.capacity}'

    def update_capacity(self,new):
        self.capacity=(new)

Vehicle1 = Vehicle( 'Volvo',180,12)
Bus1 = Bus('Bus',180,10000,50)



print(Vehicle1)
print(Bus1)

Bus1.update_capacity(100)
print(Bus1)