#from ctypes import oledll
from itertools import count

#from pygments.lexers.csound import newline

from ELO_Calculator import *
from player import Player

PlAYERS_PLAYING = []
CURRENT_ROUND = 0
k_factor = 32

def round_set_up(players_playing_in_round):
    global PlAYERS_PLAYING, CURRENT_ROUND
    CURRENT_ROUND += 1
    PlAYERS_PLAYING = players_playing_in_round
    print(f"Round: {CURRENT_ROUND} ")


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
    print(f"Elo after round {CURRENT_ROUND}")
    PlAYERS_PLAYING.sort(key=lambda player: player.temp_rank, reverse=True)
    for player in PlAYERS_PLAYING:
        diff = round(player.temp_rank - player.rank)
        player.update_rank()
        player.print_player(newLine=False)
        print(f" ({diff})")
        player.reset_games()
    print("\n")


def final_summary():
    print("="*40)
    print(f"total round : {CURRENT_ROUND} with games : {sum(len(player.all_games) for player in Player.ALL_PLAYERS)/2}\n")
    print("-"*20)
    print("Elo after all rounds")
    for player in Player.ALL_PLAYERS:
        player.print_player(newLine=False)

        print(f"[{len(player.all_games)}]")
    print("-"*20)
    print("Win ratio after all rounds ")
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
        print(f"{player.name} winrate {(wins / games) * 100:.2f}% | games({len(player.all_games)})")
    print("="*40)



def CALCUALTE_GAMES():
    global BYE

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
    final_summary()
    print()

    return Player.ALL_PLAYERS

if __name__ == "__main__":
    CALCUALTE_GAMES()

