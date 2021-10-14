class Vehicle:
    
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed =max_speed
        self.mileage = mileage

    def __str__(self):
        print(f"Vehicle model {self.name} has max speed {self.max_speed} and mileage {self.mileage}")

class Bus(Vehicle):

    def __init__(self,name , max_speed ,mileage, capacity):
        super().__init__(name,max_speed,mileage)
        self.capacity = capacity

    def __str__(self):
        print(f"Vehicle model {self.name} has max speed {self.max_speed} and mileage {self.mileage} with capacity {self.capacity}")

    def update_capacity(self,a):
        self.capacity = a

bus_1 =Bus('Minibus',150,1000,50)
bus_1.update_capacity(60)
vehicle_1 = Vehicle('honda',300 ,10000)
vehicle_1.__str__()
bus_1.__str__()
    