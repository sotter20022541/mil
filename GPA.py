import sqlite3
conne = sqlite3.connect("Credit.db")
cursor = conne.cursor()

# cursor.execute('''CREATE TABLE Cre_dit(ID TEXT,NameSub TEXT, Credit Text, Record Text)''')
# cursor.execute('''INSERT INTO Cre_dit values('59340500035', 'LNG103', '3', 'A-') ''')
# conne.commit()

cursor.execute('''SELECT * From Cre_dit''')
use = cursor.fetchall()
for i in use:
    print(i)

# def calculateGPA(Credit, record):
#         #call class and func Credit

# def cre_dit_result():
#     cursor.execute('''SELECT Credit From Credit''')
#     credit_all = cursor.fetchall()
#     box = []
#     for i in credit_all:
#         for j in i:
#             box.append(int(j))
#     return (sum(box))

#
# def cre_dit_subject():
#     cursor.execute('''SELECT Credit,Record From Credit''')
#     credit_academic = cursor.fetchall()
#     item = credit_academic[1][1]
#     print(item)
# cre_dit_subject()
