from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass

class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        if self.fuel_quantity / (self.fuel_consumption + self.AC_CONSUMPTION) >= distance:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AC_CONSUMPTION)

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    FUEL_COEF = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        if self.fuel_quantity / (self.fuel_consumption + self.AC_CONSUMPTION) >= distance:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AC_CONSUMPTION)

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * self.FUEL_COEF


