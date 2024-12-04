from unittest import TestCase
import sys
sys.path.insert(1, 'Data_models')
from poetry.repositories import Repository
import sys
from Data_models.Game import Game

class TestGame(TestCase):
    P1 = Player(name="p1")
    P2 = Player(name="p2")
    def test_to_string(self):
        global P1,P2

        g1 = Game(corp_player=P1,runner_player=P2,outcome=1)

