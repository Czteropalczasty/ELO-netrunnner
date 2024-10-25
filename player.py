class Player:
    ALL_PLAYERS = []

    def __init__(self, name):
        self.name = name
        self.rank = 1500
        self.temp_rank = 1500
        self.round_outcome = []
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