CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL,
    abbreviation TEXT NOT NULL,
    league TEXT NOT NULL
);


CREATE TABLE games (
    game_id INTEGER PRIMARY KEY,
    game_date TEXT NOT NULL,
    league TEXT NOT NULL,
    home_team_id INTEGER NOT NULL,
    away_team_id INTEGER NOT NULL,
    home_score INTEGER,
    away_score INTEGER,

    FOREIGN KEY (home_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES teams(team_id)
);


CREATE TABLE odds (
    odds_id INTEGER PRIMARY KEY,
    game_id INTEGER NOT NULL,
    sportsbook TEXT NOT NULL,
    moneyline_home INTEGER,
    moneyline_away INTEGER,
    spread_home REAL,
    spread_away REAL,
    total REAL,
    recorded_at TEXT NOT NULL,

    FOREIGN KEY (game_id) REFERENCES games(game_id)
);


CREATE TABLE predicitions (
    predicition_id INTEGER PRIMARY KEY,
    game_id INTEGER NOT NULL,
    bet_type TEXT NOT NULL,
    selection TEXT NOT NULL,
    odds INTEGER NOT NULL,
    predicted_probability REAL,
    stake REAL,
    reasoning TEXT,
    created_at TEXT NOT NULL,

    FOREIGN KEY (game_id) REFERENCES games(game_id)
);


CREATE TABLE results (
    result_id INTEGER PRIMARY KEY,
    prediciton_id INTEGER NOT NULL,
    outcome TEXT NOT NULL,
    profit_loss REAL NOT NULL,
    closing_odds INTEGER,
    settled_at TEXT NOT NULL,

    FOREIGN KEY (prediciton_id) REFERENCES predicitions(predicition_id)
);