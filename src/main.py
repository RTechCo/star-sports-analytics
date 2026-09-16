import sqlite3
from pathlib import Path


# Find the main project folder 
project_folder = Path(__file__).resolve().parent.parent

# File Locations
database_path = project_folder / "data" / "star_sports.db"
schema_path = project_folder / "database" / "schema.sql"

# Connect to the database 
connection = sqlite3.connect(database_path)

# Read our SQL schema
with open(schema_path, "r") as schema_file:
    schema = schema_file.read()

# Create the tables in the database
connection.executescript(schema)

connection.close()

print("STARPOWER Sports Analytics database created successfully!")