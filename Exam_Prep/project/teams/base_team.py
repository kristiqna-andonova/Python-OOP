from abc import ABC, abstractmethod
from typing import List

from equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0 or value.isspace():
            raise ValueError("Team name cannot be empty!")
        else:
            self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        else:
            self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        else:
            self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_equipment_price = sum([eq.price for eq in self.equipment])
        avg_protection = sum([eq.protection for eq in self.equipment]) / len(self.equipment) if self.equipment else 0
        return (f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Advantage: {self.advantage}\n"
                f" pointsBudget: {self.budget:.2f}\n"
                f"EURWins: {self.wins}\n"
                f"Total Equipment Price: {total_equipment_price:.2f}\n"
                f"Average Protection: {int(avg_protection)}")





