import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
def get_connection():
    conn = sqlite3.connect("patients.db")
    return conn

# Create a table to store patient information if it doesn't exist
def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
               CREATE TABLE IF NOT EXISTS patients (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER,
                   gender TEXT,
                   diagnosis TEXT
)
""")

    conn.commit()
    conn.close()