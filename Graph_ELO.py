# GENERATE GRAPHS
import matplotlib.pyplot as plt
from dulwich.walk import ALL_ORDERS
from Rounds import calculate_games

ALL_PLAYERS = calculate_games()

MAX_RANK =  max(ALL_PLAYERS, key=lambda player: player.rank).rank * 1.05 # i want to top be slighly under
MIN_RANK = min (ALL_PLAYERS, key=lambda player: player.rank).rank * 0.95 # i want bottom to be slighty at top

# create data from games
data = []
for player in ALL_PLAYERS:
    data.append([player.name,player.ranks])

# Create a plot
plt.figure(figsize=(10, 6))

# generate players graphs
for player_data in data:
    name = player_data[0]  # Get the name
    player_rank = player_data[1]  # Get the scores

    # index
    x_indices = range(0, len(player_rank))

    #names
    plt.plot(x_indices, player_rank, label=name, marker='o')

# Set y-axis limits
plt.ylim(MIN_RANK, MAX_RANK)

# Add labels and title
plt.xticks(x_indices)  # Ensure x-ticks match the indices
plt.xlabel("Meeting")
plt.ylabel("ELOS")
plt.title("ELO LAN: LIGA ANDROID NETRUNNER")

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)

# save the file
plt.savefig(f"Players_elo_graphs/ALL_PLAYERS.png")  # Save with the player's name as the file name
print(f"Saved ALL_PLAYERS.png")

plt.show()

for player_data in data:
    name = player_data[0]  # Get the player's name
    player_rank = player_data[1]  # Get the player's ranks (ELO scores)

    # Create a new figure for each player
    plt.figure(figsize=(8, 5))

    # Create an index for the X-axis (1, 2, 3, ...)
    x_indices = range(0, len(player_rank))

    # Plot the player's data
    plt.plot(x_indices, player_rank, label=name, marker='o', markersize=8)

    # Set y-axis limits (optional, adjust according to your data)
    plt.ylim(MIN_RANK, MAX_RANK)

    # Add labels and title specific to this player
    plt.xticks(x_indices)  # Ensure x-ticks match the indices
    plt.xlabel("Meeting")
    plt.ylabel("ELOS")
    plt.title(f"ELO LAN: {name}'s Performance Over Time")

    # Add a legend
    plt.legend()



    # Show the plot with grid
    plt.grid(True)

    # save file
    plt.savefig(f"Players_elo_graphs/{name}.png")  # Save with the player's name as the file name
    print(f"Saved {name}.png")

    plt.show()