from abc import ABC, abstractmethod
from typing import List

from project_d.food import Food


class Animal(ABC):
    ALLOWED_FOOD: List[str] = []
    WEIGHT_INCREMENT: float = 0

    def __init__(self, name, weight):
        self.name = name
        self.food_eaten = 0
        self.weight = weight

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_INCREMENT
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
