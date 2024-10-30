from itertools import count
from FileWriter import FileWriter
from Copy_generator import *
from ELO_Calculator import *
from player import Player

PlAYERS_PLAYING = []
CURRENT_ROUND = 0
k_factor = 32

def round_set_up(players_playing_in_round):
    global PlAYERS_PLAYING, CURRENT_ROUND
    CURRENT_ROUND += 1
    PlAYERS_PLAYING = players_playing_in_round

def update_elo():
    global PlAYERS_PLAYING

    for player in PlAYERS_PLAYING:
        player_games = player.round_outcome
        estimated_outcome = 0
        earned_outcome = 0
        for game in player_games:
            earned_outcome += game[1]
            estimated_outcome += get_estimated_outcome(player.rank, game[0].rank)
        player.temp_rank += get_elo_change(estimated_outcome, earned_outcome,k_factor=k_factor)

    # If player did not play simply update his rank:
    for player in Player.ALL_PLAYERS:
        if player not in PlAYERS_PLAYING:
            player.update_rank()


def round_summary():
    global CURRENT_ROUND
    PlAYERS_PLAYING.sort(key=lambda player: player.temp_rank, reverse=True)
    for player in PlAYERS_PLAYING:
        diff = round(player.temp_rank - player.rank)
        player.update_rank()
        player.to_string(newLine=False)

        player.reset_games()




def final_summary():
    FILE_PATH = "Analysis.md"
    file_writer = FileWriter(FILE_PATH)

    file_writer.write("# LAN : Liga Android:Netrunner")
    file_writer.write(">[!info] disclaimer")
    file_writer.write("> this is purely to scratch my itch, this will not determine anything in final scores, just analysis of our meetings")
    file_writer.write("\n")

    file_writer.write(">[!info] V1.1")
    file_writer.write(
        "> removed BYE games from games, does not affect elo, only winrate and h2h")
    file_writer.write("\n")

    for player in Player.ALL_PLAYERS:
        for game in player.all_games:
            if game[0].name == "BYE":
                player.all_games.remove(game)

    n_rounds = round((sum(len(player.all_games) for player in Player.ALL_PLAYERS)/2))
    file_writer.write(f"**total rounds** : {CURRENT_ROUND} with **games** : {n_rounds}\n")

    file_writer.write("## Elo after all rounds")
    file_writer.write("nick : elo [games]")
    place = 1
    for player in Player.ALL_PLAYERS:
        player_string = str(place) +". "+ player.to_string(newLine=False)
        player_string += f" [{len(player.all_games)}]"
        file_writer.write(player_string,new_line=True)
        place += 1
    file_writer.write("![all_elo_graph](Players_elo_graphs/ALL_PLAYERS.png)")

    file_writer.write("## Win ratio after all rounds ",new_line=True)
    file_writer.write("\n")

    sorted_players = sorted(
        Player.ALL_PLAYERS,
        key=lambda player: sum(1 for game in player.all_games if game[1] == 1) / len(player.all_games),
        reverse=True
    )
    for player in sorted_players:
        games = len(player.all_games)
        wins = 0

        for game in player.all_games:
            if game[1] == 1:
                wins += 1

        winrate = (wins / games) * 100

        player_string = f"> {player.name} **winrate** {winrate:.2f}% | games ({len(player.all_games)})"
        file_writer.write(player_string,new_line=True)

        def estimated_winrate(winrate, n):
            winrate /= 100

            max = winrate + 1.96 * math.sqrt((winrate * (1 - winrate) / n))
            min = winrate - 1.96 * math.sqrt((winrate * (1 - winrate) / n))


        estimated_winrate(winrate, games)


    ## Every player data
    file_writer.write("## Every player data", new_line=True)
    for player in Player.ALL_PLAYERS:

        file_writer.write(f"### {player.name}")
        winratio = sum(1 for game in player.all_games if game[1] == 1) / len(player.all_games)
        games = len(player.all_games)
        file_writer.write(f"**win ratio :** *{winratio*100:.2f}%*",new_line=True)
        file_writer.write(f"**total games :** **{games}**",new_line=True)

        # his graph
        file_writer.write(f"![{player.name} graph](Players_elo_graphs/{player.name}.png)")


        # get all players print them like this : vs Gruntownie 3-0-1 (wins,loses,draws)
        h2h_dict = {}

        played_with = set(game[0] for game in player.all_games)
        played_with = {item for item in played_with if item.name != "BYE"}
        for opponent in played_with:
            h2h_dict[opponent.name] = {
                'wins': 0,
                'losses': 0,
                'draws': 0
            }

        for game in player.all_games:
            opponent_name = game[0].name
            outcome = game[1]

            if outcome == 1:
                h2h_dict[opponent_name]["wins"] += 1
            elif outcome == 0:
                h2h_dict[opponent_name]['losses'] += 1  # Increment losses
            elif outcome == 0.5:
                h2h_dict[opponent_name]['draws'] += 1  # Increment draws
        file_writer.write("#### head to head scores", new_line=True)

        file_writer.write("(wins-losses-draws)")
        file_writer.write(f"Total : {sum(player['wins'] for player in h2h_dict.values())}-{sum(player['losses'] for player in h2h_dict.values())}-{sum(player['draws'] for player in h2h_dict.values())}")
        file_writer.write("")
        for opponent in played_with:
            file_writer.write(f"vs {opponent.name} {h2h_dict[opponent.name]['wins']}-{h2h_dict[opponent.name]['losses']}-{h2h_dict[opponent.name]['draws']} ",new_line=True)

        file_writer.write("\n")
        file_writer.write("---")

        #TODO : estimated winratio based on statistics
        #TODO : summary most games, winrates, elo, and maybe even a table?

def calculate_games():


    # generate players
    Gruntownie = Player("Gruntownie")
    GivenToFly = Player("givenToFly")
    Staniach21 = Player("Staniach21")
    Orris = Player("Orris")
    Baltar = Player("Baltar")
    Olus2000 = Player("Olus2000")
    Henader = Player("Henader")

    # creating bye player
    BYE = Player("BYE")
    BYE.rank = 0
    Player.ALL_PLAYERS.remove(BYE)

    # ROUND 1 SET UP
    round_set_up([Gruntownie, GivenToFly, Staniach21, Orris, Baltar, Olus2000])

    ## GAMES
    GivenToFly.round_outcome = [(Orris, 1), (Staniach21, 0), (Gruntownie, 1), (Olus2000, 1)]
    Gruntownie.round_outcome = [(Staniach21, 0), (Baltar, 1), (GivenToFly, 0), (Orris, 0.5)]
    Staniach21.round_outcome = [(Gruntownie, 1), (GivenToFly, 1), (Olus2000, 0), (Baltar, 0)]
    Orris.round_outcome = [(GivenToFly, 0), (Olus2000, 0), (Baltar, 0), (Gruntownie, 0.5)]
    Baltar.round_outcome = [(Olus2000, 0), (Gruntownie, 0), (Orris, 1), (Staniach21, 1)]
    Olus2000.round_outcome = [(Baltar, 1), (Orris, 1), (Staniach21, 1), (GivenToFly, 0)]

    ## update elo.
    update_elo()
    round_summary()

    # ---------------------------------------------------------------------------------------
    # ROUND 2 SET UP
    round_set_up([GivenToFly, Gruntownie, Staniach21, Orris, Olus2000])

    ## GAMES
    GivenToFly.round_outcome = [(Orris, 1), (Gruntownie, 0), (Gruntownie, 1), (BYE, 1)]
    Gruntownie.round_outcome = [(Olus2000, 1), (GivenToFly, 1), (GivenToFly, 0), (Staniach21, 0)]
    Staniach21.round_outcome = [(BYE, 1), (Olus2000, 1), (Orris, 0), (Gruntownie, 1)]
    Orris.round_outcome = [(GivenToFly, 0), (BYE, 1), (Staniach21, 1), (Olus2000, 1)]
    Olus2000.round_outcome = [(Gruntownie, 0), (Staniach21, 0), (BYE, 1), (Orris, 0)]

    ## update elo.
    update_elo()
    round_summary()

    # ---------------------------------------------------------------------------------------
    # ROUND 3 DOES NOT COUNT FOR FINAL SCORES !!!!!!!!!!1

    # ROUND 3 SET UP
    round_set_up([GivenToFly, Gruntownie, Olus2000])

    ## GAMES

    GivenToFly.round_outcome = [(Olus2000, 1), (Olus2000, 0), (Gruntownie, 1), (Gruntownie, 0)]
    Gruntownie.round_outcome = [(Olus2000, 0), (Olus2000, 0), (GivenToFly, 1), (GivenToFly, 0)]
    Olus2000.round_outcome = [(GivenToFly, 1), (GivenToFly, 0), (Gruntownie, 1), (Gruntownie, 1)]

    ## update elo.
    update_elo()
    round_summary()

    # ---------------------------------------------------------------------------------------
    # ROUND 4 DOES NOT COUNT FOR FINAL SCORES !!!!!!!!!!1

    # ROUND 4 SET UP
    round_set_up([GivenToFly, Gruntownie, Olus2000,Henader])

    ## GAMES

    GivenToFly.round_outcome = [(Olus2000, 1), (Gruntownie, 1), (Olus2000, 0), (Gruntownie, 0),(Olus2000, 0),(Olus2000, 0),(Gruntownie, 1),(Henader, 1)]
    Gruntownie.round_outcome = [(Olus2000, 0), (Olus2000, 1), (GivenToFly, 0), (GivenToFly, 1),(Henader, 1),(Henader, 1),(GivenToFly, 0)]
    Olus2000.round_outcome = [(Gruntownie, 1), (GivenToFly, 0), (Gruntownie, 0), (GivenToFly, 1),(GivenToFly, 1),(GivenToFly, 1),(Henader, 0)]
    Henader.round_outcome = [(Gruntownie,0),(Gruntownie,0),(Olus2000,1),(GivenToFly,0)]

    ## update elo.
    update_elo()
    round_summary()


    # ==============================================================================================================
    # FINAL PLAYER PRINT
    # final_summary()
    round_data = {
        "rounds":CURRENT_ROUND,
        "games":round((sum(len(player.all_games) for player in Player.ALL_PLAYERS)/2)),
        "players":[player for player in Player.ALL_PLAYERS],
        "player_games": [{
            "player_name":player.name,
            "player_games":player.all_games
        }
            for player in Player.ALL_PLAYERS]
    }

    return round_data

if __name__ == "__main__":
    calculate_games()

