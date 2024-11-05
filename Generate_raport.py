from FileWriter import FileWriter
from player import Player
FILE_PATH = "Analysis.md"
from Rounds import *

def generate_rapport():
    # Get data
    game_data = calculate_games()
    file_writer = FileWriter(FILE_PATH)

    # 1st paragraph
    file_writer.write("# LAN : Liga Android:Netrunner")
    file_writer.write(">[!info] disclaimer")
    file_writer.write("> this is purely to scratch my itch, this will not determine anything in final scores, just analysis of our meetings")
    file_writer.write("\n")

    file_writer.write(">[!info] V1.1")
    file_writer.write(
        "> removed BYE games from games, does not affect elo, only winrate and h2h")
    file_writer.write("\n")


    file_writer.write(f"**total rounds** : {game_data['rounds']} with **games** : {game_data['games']}\n")

    file_writer.write("## Elo after all rounds")
    file_writer.write("nick : elo [games]")
    place = 1
    for player in game_data["players"]:
        player_string = str(place) +". "+ player.to_string(newLine=False)
        player_string += f" [{len(player.all_games)}]"
        file_writer.write(player_string)
        place += 1
    file_writer.write("![all_elo_graph](Players_elo_graphs/ALL_PLAYERS.png)")

    file_writer.write("## Win ratio after all rounds ")
    file_writer.write("\n")

    sorted_players = sorted(
        game_data["players"],
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
        print(f"player currently done is {player.name} he played with :")

        for playerz in played_with:
            print(playerz.name)

        print(f"{player.name} games are ")
        for game in player.all_games:
            print(f"vs {game[0].name}score {game[1]}")

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
        def estimated_winrate(winrate, n):
            winrate /= 100

            max = winrate + 1.96 * math.sqrt((winrate * (1 - winrate) / n))
            min = winrate - 1.96 * math.sqrt((winrate * (1 - winrate) / n))

            print(f"es {player.name}  min: {min*100:.2f}%, max: {max*100:.2f}%")

        estimated_winrate(winrate, games)
        #TODO : summary most games, winrates, elo, and maybe even a table?

        copy_all_analysis()


if __name__ == "__main__":
    generate_rapport()