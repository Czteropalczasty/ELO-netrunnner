class Player:
    ALL_PLAYERS = []

    def __init__(self, name,rank=1500):
        self.name = name
        self.rank = rank
        self.temp_rank = 1500
        self.round_outcome = []
        self.all_games = []
        self.ranks = [self.rank]

        Player.ALL_PLAYERS.append(self)
    def update_rank(self):
        self.rank = self.temp_rank
        self.ranks.append(self.rank)
        Player.ALL_PLAYERS.sort(key=lambda player: player.rank,reverse=True)

    def print_player(self,newLine=True):
        string = (f"{self.name} : {round(self.rank)}")
        if newLine:
            string+=("\n")
        return string

    def reset_games(self):
        self.all_games += self.round_outcome
        self.round_outcome = []