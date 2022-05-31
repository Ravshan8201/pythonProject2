import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
F_Name STRING ,
Phone_Num INTEGER,
DOMTYPE STRING,
DOM STRING,
LAV STRING,
STATUS STRING,
EDU STRING,
EDUPLACE STRING,
DOM1 STRING,
EDUPLACE1 STRING,
QJOB STRING,
EXJOB STRING,
RJOB STRING,
LANGSTAGE STRING,
S_NUM STRING,
DOP STRING,
DOP2 STRING,
BB STRING,
TT STRING,
Lang INTEGER ,
Stage INTEGER

)
""")
first_insert = """
INSERT INTO Users VALUES ("{}", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "{}" )
"""
upd_EDUPLACE = """
UPDATE Users 
SET EDUPLACE = "{}" 
WHERE TG_ID = "{}"
"""
select_EDUPLACE = """
SELECT EDUPLACE 
From Users
WHERE TG_ID = "{}"
"""

upd_DOM1 = """
UPDATE Users 
SET DOM1= "{}" 
WHERE TG_ID = "{}"
"""
select_DOM1 = """
SELECT DOM1
From Users
WHERE TG_ID = "{}"
"""

upd_EDUPLACE1 = """
UPDATE Users 
SET EDUPLACE1= "{}" 
WHERE TG_ID = "{}"
"""
select_EDUPLACE1 = """
SELECT EDUPLACE1
From Users
WHERE TG_ID = "{}"
"""

upd_QJOB = """
UPDATE Users 
SET QJOB ="{}" 
WHERE TG_ID = "{}"
"""
select_QJOB = """
SELECT QJOB
From Users
WHERE TG_ID = "{}"
"""

upd_EXJOB = """
UPDATE Users 
SET EXJOB= "{}" 
WHERE TG_ID = "{}"
"""
select_EXJOB = """
SELECT EXJOB
From Users
WHERE TG_ID = "{}"
"""
upd_RJOB = """
UPDATE Users 
SET RJOB ="{}" 
WHERE TG_ID = "{}"
"""
select_RJOB = """
SELECT RJOB
From Users
WHERE TG_ID = "{}"
"""

upd_LANGSTAGE = """
UPDATE Users 
SET LANGSTAGE= "{}" 
WHERE TG_ID = "{}"
"""
select_LANGSTAGE = """
SELECT LANGSTAGE
From Users
WHERE TG_ID = "{}"
"""

upd_S_NUM = """
UPDATE Users 
SET S_NUM= "{}" 
WHERE TG_ID = "{}"
"""
select_S_NUM = """
SELECT S_NUM
From Users
WHERE TG_ID = "{}"
"""

upd_DOP = """
UPDATE Users 
SET DOP ='{}' 
WHERE TG_ID = "{}"
"""
select_DOP = """
SELECT DOP
From Users
WHERE TG_ID = "{}"
"""

upd_DOP2 = """
UPDATE Users 
SET DOP2 ="{}" 
WHERE TG_ID = "{}"
"""
select_DOP2 = """
SELECT DOP2
From Users
WHERE TG_ID = "{}"
"""

upd_BB = """
UPDATE Users 
SET BB= "{}" 
WHERE TG_ID = "{}"
"""
select_BB = """
SELECT BB
From Users
WHERE TG_ID = "{}"
"""

upd_TT = """
UPDATE Users 
SET TT= "{}" 
WHERE TG_ID = "{}"
"""
select_TT = """
SELECT TT
From Users
WHERE TG_ID = "{}"
"""

# upd_ = """
# UPDATE Users
# SET  "{}"
# WHERE TG_ID = "{}"
# """
# select_ = """
# SELECT
# From Users
# WHERE TG_ID = "{}"
# """




upd_DOM = """
UPDATE Users 
SET DOM="{}" 
WHERE TG_ID = "{}"
"""
select_DOM = """
SELECT DOM
From Users
WHERE TG_ID = "{}"
"""

upd_LAV = """
UPDATE Users 
SET LAV = "{}" 
WHERE TG_ID = "{}"
"""
select_LAV = """
SELECT LAV
From Users
WHERE TG_ID = "{}"
"""

upd_STATUS = """
UPDATE Users 
SET STATUS = "{}" 
WHERE TG_ID = "{}"
"""
select_STATUS = """
SELECT STATUS
From Users
WHERE TG_ID = "{}"
"""


upd_EDU = """
UPDATE Users 
SET EDU = "{}" 
WHERE TG_ID = "{}"
"""
select_EDU = """
SELECT EDU
From Users
WHERE TG_ID = "{}"
"""

upd_DOMTYPE = """
UPDATE Users 
SET DOMTYPE = "{}" 
WHERE TG_ID = "{}"
"""
select_DOMTYPE = """
SELECT DOMTYPE
From Users
WHERE TG_ID = "{}"
"""


upd_TT = """
UPDATE Users 
SET TT = "{}" 
WHERE TG_ID = "{}"
"""
select_TT = """
SELECT TT
From Users
WHERE TG_ID = "{}"
"""

upd_BB = """
UPDATE Users 
SET BB = "{}" 
WHERE TG_ID = "{}"
"""
select_BB = """
SELECT BB
From Users
WHERE TG_ID = "{}"
"""

get_id = """
SELECT TG_ID 
FROM Users
Where TG_ID = "{}"
"""
upd_name = """
UPDATE Users 
SET F_Name = "{}" 
WHERE TG_ID = "{}"
"""
select_name = """
SELECT F_Name
From Users
WHERE TG_ID = "{}"
"""

update_phone_num = """
UPDATE Users 
SET Phone_Num = "{}"
WHERE TG_ID = "{}"
"""
select_num = """
SELECT Phone_Num 
FROM Users
WHERE TG_ID = "{}"
"""


lang = """
UPDATE Users
SET lang = "{}"
WHERE TG_ID = "{}"
"""
lang_select = """
SELECT Lang
FROM Users
WHERE TG_ID = "{}"
"""

stagee = """
UPDATE Users
SET Stage = "{}"
WHERE TG_ID = "{}"
"""
stage = """
SELECT Stage
FROM Users
WHERE TG_ID = "{}"
"""

conn.commit()