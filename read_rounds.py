import json
import os
from pprint import pprint
from player import Player
# iterate over every round
# gather data
# calculate elo of a player after round x, update players.json
rounds = []
players = []

# get players
with open("data/players.json") as players_json:
    players_dict = json.load(players_json)
    for player in players_dict["players"]:
        new_player = Player(player['name'],player['rank'][0])
        new_player.ranks = player['rank']
        players.append(new_player)

# iterate over every round except for template, and players
directory = 'data'
files = os.listdir(directory)
files.remove("round_template.json")
files.remove("players.json")

for filename in files:
    file_path = os.path.join(directory, filename)
    with open(file_path) as round_json:
        json_from_file = json.load(round_json)
        rounds.append(json_from_file)

# we have all rounds in json
for round_ in rounds:
    round_number = round_['meeting number']
    #TODO:
    # 1. get players playing in a round, set their ranks
    # 2. for each round get plays and games
    # 3. update data, and print
    pprint(round_)