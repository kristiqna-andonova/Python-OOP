from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player___: Player):
        if player___.guild == "Unaffiliated":
            player___.guild = self.name
            self.players.append(player___)
            return f"Welcome player {player___.name} to the guild {self.name}"
        elif player___.guild == self.name:
            return "Player {player_name} is already in the guild."
        else:
            return f"Player {player___.name} is in another guild."

    def kick_player(self, player_name: str):
        for player_ in self.players:
            if player_ == player_name:
                player_.guild = "Unaffiliated"
                self.players.remove(player_)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        output = [f"Guild: {self.name}"]
        for player__ in self.players:
            output.append(player__.player_info())
        return "\n".join(output)


