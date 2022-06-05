import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS J (
RU STRING ,
UZ STRING ,
ENG STRING

)
""")
first_insertjJJ = """
INSERT INTO J VALUES ("{}", "{}", "{}")
"""
