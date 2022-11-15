import requests
from datetime import datetime
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    
    

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)
    
    print(f"Players from FIN {datetime.now()}")
    print(" ")
    

    for player in players:
        if "FIN" in player.nationality:
            print(player)
if __name__ == "__main__":
    main()