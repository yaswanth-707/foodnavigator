import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS food_centers (
    name TEXT NOT NULL,
    area TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    food_type TEXT,
    average_price INTEGER,
    opening_time TEXT,
    closing_time TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")