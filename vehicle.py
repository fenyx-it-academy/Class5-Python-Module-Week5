class Vehicle:#I created a Vehicle class with name, max_speed and mileage instance attributes
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def __str__(self): #I added function __str__ to vehicle class and print the info about vehicle as
        return f"Vehicle {self.name} has max speed {self.max_speed} and mileage {self.mileage}"

class Bus(Vehicle): # I created a child class Bus that will inherit all of the variables and methods of the Vehicle class
    def __init__(self, name, max_speed, mileage,capacity):#I added attribute capacity to class Bus
        super().__init__(name, max_speed, mileage)
        self.capacity=capacity
    
    def __str__(self):# It is going to write this info about the bus with capacity
        return f"Bus {self.name} has max speed {self.max_speed} and mileage {self.mileage} with capacity {self.capacity}"

    def update_capacity(self,new_capacity):# i defined a new method and updated the capacity attribute
        self.capacity=new_capacity

vehicle=Vehicle("mercedes",270,4000)# I created a vehicle and bus object and print them
bus=Bus("volvo",200,1000,100)
print(vehicle)
print(bus)
bus.update_capacity(200)# I updated the capacity with the update_capacity method and print it
print(bus)