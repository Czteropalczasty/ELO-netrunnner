#TODO:
# 1. store games in both players, just by adding game to 1
# 2. store rounds and games in rounds
# 3. functions getters and setters

class Player:
    ALL_PLAYERS = []

    def __init__(self, name,rank=1500):
        self.name = name
        self.rank = rank
        self.temp_rank = rank
        self.round_outcome = []
        self.all_games = []
        self.ranks = [self.rank]
        self.rounds = {}

        Player.ALL_PLAYERS.append(self)
    def update_rank(self):
        self.rank = self.temp_rank
        self.ranks.append(self.rank)
        Player.ALL_PLAYERS.sort(key=lambda player: player.rank,reverse=True)

    def to_string(self, newLine=True):
        string = (f"{self.name} : {round(self.rank)}")
        if newLine:
            string+=("\n")
        return string

    def reset_games(self):
        self.all_games += self.round_outcome
        self.round_outcome = []

    def create_round(self,round_number:int):
        self.rounds[str(round_number)] = []
