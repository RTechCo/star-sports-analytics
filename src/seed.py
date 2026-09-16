import sqlite3
from pathlib import Path

projecr_folder = Path(__file__).resolve().parent.parent
database_path = projecr_folder / "data" / "star_sports.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

teams = [
    (1, "Los Angeles Lakers", "LAL", "NBA"),
    (2, "Golden State Warriors", "GSW", "NBA"),
    (3, "Minnesota Timberwolves", "MIN", "NBA"),
    (4, "Boston Celtics", "BOS", "NBA"),
    (5, "Denver Nuggets", "DEN", "NBA"),
]

cursor.executemany(
    """INSERT OR IGNORE INTO teams(team_id, team_name, abbreviation, league) VALUES (?, ?, ?, ?)""",
    teams
)

connection.commit()

cursor.execute("SELECT * FROM teams")
saved_teams = cursor.fetchall()

for team in saved_teams:
    print(team)

connection.close()

print("\nTeams added successfully!")
 