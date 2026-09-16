import sqlite3
from pathlib import Path
from datetime import datetime

project_folder = Path(__file__).resolve().parent.parent
database_path = project_folder / "data" / "star_sports.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

game_id = 1  # Replace with the actual game_id for which you want to add odds

cursor.execute(
    """INSERT INTO odds (game_id, sportsbook, moneyline_home, moneyline_away, spread_home, spread_away, total, recorded_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
    (game_id, "TEST SPORTSBOOK", -150, 130, -3.5, 3.5, 224.5, datetime.now().isoformat(timespec="seconds"))
)

connection.commit()
connection.close()

print("Odds added successfully!")