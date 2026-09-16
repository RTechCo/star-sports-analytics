import sqlite3
from pathlib import Path

def implied_probability(american_odds):
    if american_odds < 0:
        return abs(american_odds) / (abs(american_odds) + 100)
    else:
        return 100 / (american_odds + 100)

project_folder = Path(__file__).resolve().parent.parent
database_path = project_folder / "data" / "star_sports.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute(
    """SELECT games.game_id, home.team_name, away.team_name, odds.sportsbook, odds.moneyline_home, odds.moneyline_away FROM games JOIN teams AS home ON games.home_team_id = home.team_id JOIN teams AS away ON games.away_team_id = away.team_id JOIN odds ON games.game_id = odds.game_id WHERE games.game_id = 1 ORDER BY odds.recorded_at DESC LIMIT 1""")

game = cursor.fetchone()

if game:
    game_id, home_team, away_team, sportsbook, home_odds, away_odds = game
    home_probability = implied_probability(home_odds)
    away_probability = implied_probability(away_odds)

    total = home_probability + away_probability

    fair_home = home_probability / total
    fair_away = away_probability / total 

    print("\n--- STARPOWER SPORTS ANALYTICS ---")
    print(f"Game #{game_id}")
    print(f"{away_team} @ {home_team}")
    print(f"Sportsbook: {sportsbook}")

    print("\nMoneyline")
    print(f"{home_team}: {home_odds:+}")
    print(f"{away_team}: {away_odds:+}")

    print("\nNo-Vig Market Probability")
    print(f"{home_team}: {fair_home:.2%}")
    print(f"{away_team}: {fair_away:.2%}")

else:
    print("No game or odds found.")

    connection.close()     
