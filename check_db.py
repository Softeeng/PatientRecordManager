import sqlite3

conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

# Check if patient table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in database:", cursor.fetchall())

conn.close()