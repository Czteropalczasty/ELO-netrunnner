import json
import os

# iterate over every round
# gather data
# calculate elo of a player after round x, update players.json
rounds = []


# iterate over every round except for template
directory = 'data'
files = os.listdir(directory)
files.remove("round_template.json")
files.remove("players.json")

for filename in files:
    file_path = os.path.join(directory, filename)
    with open(file_path) as round_json:
        json_from_file = json.load(round_json)
        rounds.append(json_from_file)

