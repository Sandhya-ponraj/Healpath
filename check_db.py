import sqlite3

conn = sqlite3.connect("healpath.db")
cur = conn.cursor()

cur.execute("PRAGMA table_info(assessments)")
columns = cur.fetchall()

print("Columns in assessments table:\n")

for col in columns:
    print(col)

conn.close()