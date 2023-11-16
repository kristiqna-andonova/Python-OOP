from equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self, protection=90, price=25.0):
        super().__init__(protection, price)
        self.protection = protection
        self.price = price

    def increase_price(self):
        self.price *= 1.1

