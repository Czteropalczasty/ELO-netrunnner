class Player:
    ALL_PLAYERS = []

    def __init__(self, name,rank=None):
        self.name = name
        if rank is None:
            self.rank = 1500
        else:
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
        print(f"{self.name} : {round(self.rank)}",end="")
        if newLine:
            print("")

    def reset_games(self):
        self.all_games += self.round_outcome
        self.round_outcome = []