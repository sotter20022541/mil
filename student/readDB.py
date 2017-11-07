import sqlite3
import sys

conn = sqlite3
conn = sqlite3.connect('IDPassStudent.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM IDPASS")
    rows = cur.fetchall()
    for row in rows:
        print(row)
