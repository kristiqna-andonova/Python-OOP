from equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self, protection=120, price=15.0):
        super().__init__(protection, price)
        self.protection = protection
        self.price = price

    def increase_price(self):
        self.price *= 1.2





