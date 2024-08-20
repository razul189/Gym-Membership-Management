import sqlite3

DATABASE_NAME = 'gym_database.db'

CONN = sqlite3.connect(DATABASE_NAME)
CURSOR = CONN.cursor()

def create_tables():
    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS gyms (
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT,
        opening_hours TEXT,
        closing_hours TEXT
    )
    """)
    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        gender TEXT,
        membership_type TEXT CHECK (membership_type IN ('basic', 'silver', 'gold')),
        gym_id INTEGER,
        FOREIGN KEY (gym_id) REFERENCES gyms(id)
    )
    """)
    CONN.commit()

    create_tables()

