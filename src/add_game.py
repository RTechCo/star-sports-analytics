import sqlite3
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database_path = project_folder / "data" / "star_sports.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO games (game_date, league, home_team_id, away_team_id) VALUES (?, ?, ?, ?)""",
    ("2026-09-16", "NBA", 1, 2)
)

connection.commit()

game_id = cursor.lastrowid

print(f"Game #{game_id} added successfully!")

connection.close()