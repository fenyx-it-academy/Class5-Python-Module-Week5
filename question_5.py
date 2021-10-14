class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

    def __str__(self):
        return(f"Vehicle Model {self.name}, max speed {self.max_speed} and milage {self.milage}")
class Bus(Vehicle):
    def __init__(self, name, max_speed, milage,capacity):
        super().__init__(name, max_speed, milage)
        self.capacity = capacity

    def __str__(self):
        return(f"Bus {self.name} has max speed {self.max_speed} and mileage {self.milage} with capacity {self.capacity}")

    def update_capacity(self,update):
        self.capacity = update

v = Vehicle("X",180,12)
b = Bus("Light",170,50,100)
print(v)
print(b)

b.update_capacity(99)
print(b)