from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    AIR_CONSUMPTION = 0.9

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AIR_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONSUMPTION = 1.6
    REFUEL_EFFICIENCY = 0.95

    # def __init__(self, fuel_quantity, fuel_consumption):
    #     self.fuel_quantity = fuel_quantity
    #     self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AIR_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.REFUEL_EFFICIENCY


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
