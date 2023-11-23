from project.
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    valid_loans = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    valid_clients = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.valid_loans:
            raise Exception("Invalid loan type!")

        new_loan = self.valid_loans[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.valid_clients:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.valid_clients[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = self._find_loans_by_type(loan_type)[0]
        client = self._find_client_by_id(client_id)
        if not client.possible_type == loan_type:
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self._find_client_by_id(client_id)

        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        filtered_loans = self._find_loans_by_type(loan_type)
        [l.increase_interest_rate() for l in filtered_loans]
        return f"Successfully changed {len(filtered_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        clients_rate = self._find_client_by_interest(min_rate)
        [c.increase_clients_interest() for c in clients_rate]
        return f"Number of clients affected: {len(clients_rate)}."

    def get_statistics(self):
        total_income = sum([client.income for client in self.clients])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        granted_amount = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_rate = sum([client.interest for client in self.clients]) / len(
            self.clients) if self.clients else 0

        return f"""Active Clients: {len(self.clients)}
Total Income: {total_income:.2f}
Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_rate:.2f}"""

    def _find_client_by_interest(self, min_rate):
        return [c for c in self.clients if c.interest < min_rate]

    def _find_client_by_id(self, client_id):
        client = [client for client in self.clients if client.client_id == client_id]
        return client[0] if client else None

    def _find_loans_by_type(self, loan_type):
        return [loan for loan in self.loans if loan.__class__.__name__ == loan_type]