from unittest import TestCase
from ELO_Calculator import get_estimated_outcome, get_elo_change
from netrunner_league_monte_carlo import player, players


class Player:
    def __init__(self, name):
        self.name = name
        self.rank = 1500
        self.round_outcome = []


class Test(TestCase):
    def test_get_estimated_outcome(self):
        rank_a = 1613
        games = [(1609,0), (1477,0.5), (1388,1), (1586,1), (1720,0)]
        estimated_earn= 0
        actual_earn = sum([i[1] for i in games])
        for game in games:
            estimated_earn += get_estimated_outcome(1613,game[0])

        elo_change = get_elo_change(estimated_earn, actual_earn)
        rank_a += elo_change
        self.assertEqual(round(rank_a),1601)


class Test(TestCase):
    def test_jacob_elo(self):
        Gruntownie = Player("Gruntownie")
        GivenToFly = Player("givenToFly")
        Staniach21 = Player("Staniach21")
        Orris = Player("Orris")
        Baltar = Player("Baltar")
        Olus2000 = Player("Olus2000")

        players = []
        players.append(Gruntownie)
        players.append(GivenToFly)
        players.append(Staniach21)
        players.append(Orris)
        players.append(Baltar)
        players.append(Olus2000)

        # round 1
        GivenToFly.round_outcome = [(Orris,1),(Staniach21,0),(Gruntownie,1),(Olus2000,1)]
        Gruntownie.round_outcome = [(Staniach21,0),(Baltar,1),(GivenToFly,0),(Orris,0.5)]
        Staniach21.round_outcome = [(Gruntownie,1),(GivenToFly,1),(Olus2000,0),(Baltar,0)]
        Orris.round_outcome = [(GivenToFly,0),(Olus2000,0),(Baltar,0),(Gruntownie,0.5)]
        Baltar.round_outcome = [(Olus2000,0),(Gruntownie,0),(Orris,1),(Staniach21,1)]
        Olus2000.round_outcome = [(Baltar,1),(Orris,1),(Staniach21,1),(GivenToFly,0)]

        #update elo.
        for player in players:
            player_games = player.round_outcome
            estimated_outcome = 0
            earned_outcome = 0
            for game in player_games:
                earned_outcome += game[1]
                estimated_outcome += get_estimated_outcome(player.rank,game[0].rank)
            print(f"earner outcome {earned_outcome} estimated is {estimated_outcome} ")
        # round 2

