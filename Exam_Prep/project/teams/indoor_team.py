from teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    BUDGET = 500.0
    INCREMENT_ADVANTAGE = 145

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.advantage += self.INCREMENT_ADVANTAGE
        self.wins += 1
