from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate  # lihven procent
        self.amount = amount  # suma

    @abstractmethod
    def increase_interest_rate(self):  # Metodut uvelichava likhveniya protsent po zaema
        pass

