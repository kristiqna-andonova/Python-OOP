from loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    interest_rate_ = 3.5
    amount_ = 50_000.0


    def __init__(self):
        super().__init__(interest_rate=self.interest_rate_, amount=self.amount_)

    def increase_interest_rate(self):
        self.interest_rate += 0.5