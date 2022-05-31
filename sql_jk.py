import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS JOBSTAGE(
TG_ID STRING ,
JOB STRING ,
STATUS STRING
)
""")
first_insertjs = """
INSERT INTO JOBSTAGE VALUES ("{}", "{}", "{}")
"""
upd_JOB = """
UPDATE JOBSTAGE 
SET JOB = "{}" 
WHERE TG_ID = "{}"
"""
select_JOB = """
SELECT JOB 
From JOBSTAGE
WHERE TG_ID = "{}"
"""

upd_STATUS = """
UPDATE JOBSTAGE 
SET STATUS = "{}" 
WHERE TG_ID = "{}" AND JOB = "{}"
"""