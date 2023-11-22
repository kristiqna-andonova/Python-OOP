from loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    interest_rate_ = 1.5
    amount_ = 2000.0


    def __init__(self):
        super().__init__(interest_rate=self.interest_rate_, amount=self.amount_)

    def increase_interest_rate(self):
        self.interest_rate += 0.2


    