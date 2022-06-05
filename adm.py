import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS ADM (
TG_ID INTEGER 
)
""")
first_insertj = """
INSERT INTO ADM VALUES ("{}")
"""
