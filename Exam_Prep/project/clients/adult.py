from clients.base_client import BaseClient


class Adult(BaseClient):
    possible_type = "MortgageLoan"

    def increase_clients_interest(self):
        self.interest += 2.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=4.0)