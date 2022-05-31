import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Job_But(
RU STRING ,
UZ STRING ,
ENG STRING,
BUT_STAGE STRING,
SEC_STAGE STRING,
STATUS STRING
)
""")
first_insertj = """
INSERT INTO Job_But VALUES ("{}", " ", " ", " ", " ", " ")
"""

upd_SEC_STAGE = """
UPDATE Job_But 
SET SEC_STAGE = "{}" 
WHERE {} = "{}"
"""
select_SEC_STAGE = """
SELECT SEC_STAGE 
From Job_But
WHERE {} = "{}"
"""


upd_BUT_STAGE = """
UPDATE Job_But 
SET BUT_STAGE = "{}" 
WHERE {} = "{}"
"""
select_BUT_STAGE = """
SELECT BUT_STAGE 
From Job_But
WHERE {} = "{}"
"""


upd_RU = """
UPDATE Job_But 
SET RU = "{}" 
WHERE {} = "{}"
"""
select_RU = """
SELECT RU 
From Job_But
WHERE {} = "{}"
"""

upd_UZ = """
UPDATE Job_But 
SET UZ = "{}" 
WHERE {} = "{}"
"""
select_UZ = """
SELECT UZ 
From Job_But
WHERE {} = "{}"
"""

upd_ENG = """
UPDATE Job_But 
SET ENG = "{}" 
WHERE {} = "{}"
"""
select_ENG = """
SELECT ENG 
From Job_But
WHERE {} = "{}"
"""