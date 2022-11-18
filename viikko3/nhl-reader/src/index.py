from player_stats import PlayerStats
from player_reader import PlayerReader
import requests
from datetime import datetime
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    
    

   
    print(f"Players from FIN {datetime.now()}")
    print(" ")
    

    for player in players:
        print(player)
        
if __name__ == "__main__":
    main()