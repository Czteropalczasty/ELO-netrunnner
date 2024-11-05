from math import gamma


class Game:
    ALL_GAMES = []

    def __init__(self, corp_player,runner_player,outcome):
        """
           creates

           Args:
               corp_player (Player): Description of parameter `param1`.
               runner_player (Player): Description of parameter `param2`.
               outcome (Int): 1 is for corp win, 0 for runner win, 0.5 for a draw.

           Returns:
               return_type: Description of the return value.

           Raises:
               ExceptionType: Description of when this exception is raised.
           """


        self.corp_player = corp_player
        self.runner_player = runner_player
        self.outcome = outcome
        Game.ALL_GAMES.append(self)

    def to_string(self, newLine=True):
        outcome_to_string = {
            1:"1-0",
            0.5:"0.5-0.5",
            0:"0-1"
        }

        string = f"{self.corp_player} {outcome_to_string[self.outcome]} {self.runner_player}"
        if newLine:
            string+= "\n"
        return string

