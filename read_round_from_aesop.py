import json
import os
import re
from player import Player
from ELO_Calculator import *

directory = 'data/aesop'
files = os.listdir(directory)
outcome_dict_from_corp_normalisation = {
    3:1,
    1:0.5,
    0:0
}

def find_player_by_nick(nick, players):
    for person in players:
        if person.name == nick:
            return person
    return None  # If no match is found


rounds = []
for filename in files:
    file_path = os.path.join(directory, filename)
    with open(file_path) as round_json:
        json_from_file = json.load(round_json)
        rounds.append(json_from_file)


for game_round in rounds:


    players = []
    round_number = 0

    # get round number
    round_number = game_round['event']['name']
    number = int(re.search(r'\d+$', round_number).group())
    round_number = int(number)

    # get players :
    for player in game_round['players']:
        player_name = player['player']
        player_rank = 1500 #TODO: get from players.json rank for current round
        new_player = Player(player_name,player_rank)
        players.append(new_player)

    # play all games
    rounds = game_round['rounds']
    all_games = [game for round_ in rounds for game in round_]
    for game in all_games:
        # find players
        corpPlayer_name = game['corpPlayer']
        runnerPlayer_name = game['runnerPlayer']
        corpPlayer = find_player_by_nick(corpPlayer_name, players)
        runnerplayer = find_player_by_nick(runnerPlayer_name, players)
        # match players
        outcome_for_corp = outcome_dict_from_corp_normalisation[game['corpScore']]
        outcome_for_runner = outcome_dict_from_corp_normalisation[game['runnerScore']]

        # update round_outcome
        corpPlayer.round_outcome.append((runnerplayer, outcome_for_corp))
        runnerplayer.round_outcome.append((corpPlayer,outcome_for_runner))


    for player in players:
        player_games = player.round_outcome
        estimated_outcome = 0
        earned_outcome = 0
        for game in player_games:
            earned_outcome += game[1]
            estimated_outcome += get_estimated_outcome(player.rank, game[0].rank)
        player.temp_rank += get_elo_change(estimated_outcome, earned_outcome,k_factor=32)

        # If player did not play simply update his rank:
    for player in Player.ALL_PLAYERS:
        player.update_rank()

    print(f"Elo after round {round_number}")
    players.sort(key=lambda player: player.temp_rank, reverse=True)
    for player in players:
        diff = round(player.temp_rank - player.rank)
        player.update_rank()
        player.to_string(newLine=False)
        print(f" ({diff})")
    print("\n")

    franek = find_player_by_nick("Gruntownie",players)
    for game in franek.round_outcome:
        print(f"vs {game[0].name} : {game[1]}")


