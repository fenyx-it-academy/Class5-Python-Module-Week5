"""Create a Vehicle class with name, max_speed and mileage instance attributes
--Add function __str__ to vehicle class and print the info about vehicle as: 
   "Vehicle Model X has max speed 180 and mileage 12"
--Create a child class Bus that will inherit all of the variables and methods 
of the Vehicle class
--Add attribute capacity to class Bus
--Update Bus class such that print message will be: Bus Breng has max speed 
180 and mileage 50 with capacity 100 (Hint: Override _str_ method)
--Add update_capacity() method to the class Bus
--Create a Vehicle and a Bus object and print both of them
call update_capacity() method for the earlier created Bus object and print it,
see the difference"""



class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def __str__(self):
        return f"Vehicle:{self.name} has max speed {self.max_speed}km and mileage {self.mileage}."


class Bus(Vehicle):  #inherits Vehicle and add capacity in Bus additionally
    def __init__(self, name, max_speed, mileage,capacity):
        Vehicle.__init__(self,name, max_speed, mileage)
        self.capacity=capacity
    def __str__(self): # we override ___str__ for Bus class,capacity will be added
        return f"Bus:{self.name} has max speed {self.max_speed}km and mileage {self.mileage} with capacity {self.capacity}."

    def updated_capacity(self,updated_capacity):  #to upgrade capacity
        self.capacity=updated_capacity

V=Vehicle("Ford",200,11)
B=Bus("Man",200,20,40)

print(V)
print(B)
B.updated_capacity(50)  #upgraded capacity as 50 for B
print(B)
