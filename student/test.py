import sqlite3
from Profile import Profile
pro = Profile('{}.db'.format())
conne = pro.conne()
conne.row_factory = sqlite3.Row
cursor = conne.cursor()
cursor.execute("SELECT * FROM PROFILE")
roww = cursor.fetchone()
pro.name(roww)
