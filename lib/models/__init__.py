import sqlite3

CONN = sqlite3.connect('gym_database.db')
CURSOR = CONN.cursor()
