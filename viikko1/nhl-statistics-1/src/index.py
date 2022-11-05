from player_reader import PlayerReader
from statistics import Statistics
from statistics import SortBy

def main():
    stats = Statistics(PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"))
    
    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)

    
    for player in stats.top(10):
        print(player)

    
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)


if __name__ == "__main__":
    main()
