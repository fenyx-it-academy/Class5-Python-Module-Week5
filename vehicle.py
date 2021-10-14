class Vehicle:
        def __init__(self,name,max_speed,mileage):
                self.name=name
                self.max_speed=max_speed
                self.mileage=mileage

        def __str__(self):
                self.vehicle_info=("Vehicle Model X has max speed 180 and mileage 12")
                
                return self.vehicle_info
class Bus(Vehicle):
        def __init__(self, name, max_speed, mileage,capacity):
                super().__init__(name, max_speed, mileage)
                self.capacity=capacity
        def __str__(self):
                self.bus_info=("Bus Breng has max speed 180 and mileage 50 with capacity 100")
                return self.bus_info
        def update_capacity(self):
                print(f"Name:{self.name},Max speed:{self.max_speed},Mileage:{self.mileage}, capacity:{self.capacity} Vehicle info: {bus_1.__str__()}")


bus_1=Bus("best bus","100 kmph",5,"40 persons")
bus_1.update_capacity()

vehicle_1=Vehicle("plane","1,510 mph",10)
print(vehicle_1.__str__())