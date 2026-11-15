class Player:
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

    def __str__(self):
        return (
            f"{self.player_id}, Name: {self.name}, Role: {self.role}, "
            f"Franchise: {self.franchise}, Credits: {self.credits}"
        )


class FantasyTeam:
    """A fantasy XI picked by one person."""

    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
        total = 0
        for player in self.players:
            total = total + player.credits
        return total

    def count_by_role(self):
        counts = {"WK": 0, "BAT": 0, "AR": 0, "BOWL": 0}
        for player in self.players:
            counts[player.role] = counts[player.role] + 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def most_expensive(self):
        if not self.players:
            return None

        most_expensive = self.players[0]
        for player in self.players[1:]:
            if player.credits > most_expensive.credits:
                most_expensive = player
        return most_expensive

    def remaining_budget(self):
        return 100 - self.total_credits()

    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner: {self.owner}, {size} players, {cost} cr)"


babar = Player("P089", "Babar Azam", "BAT", "Peshawar Zalmi", 10.5)

print(babar)