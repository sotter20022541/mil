import sqlite3
class Profile:
    def __init__(self,file):
        self.file = file

    def conne(self):
        return sqlite3.connect("{}".format(self.file))

    def idstudent(self,row):
        print("ID = ",row[0])
        return row[0]

    def name(self,row):
        print("name = ",row[1])
        return row[1]

    def date(self,row):
        print(" Date of birth = ",row[2])
        return row[2]

    def birthplace(self,row):
        print("Birthplace = ",row[3])
        return row[3]

    def nation(self,row):
        print("Nationality = ",row[4])
        return row[4]

    def education(self,row):
        print("Education = ",row[5])
        return row[5]

    def disease(self,row):
        print("Disease = ",row[6])
        return row[6]

    def relative(self,row):
        print("Relative = ",row[7])
        return row[7]

    def phone(self,row):
        print("Phone = ",row[8])
        return row[8]

    def address(self,row):
        print("Address = ",row[9])
        return row[9]

    def email(self,row):
        print("E-maill = ",row[10])
        return [10]

    def alldata(self,row):
        for item in row:
            print(item)


# cursor = conne.cursor()
# cursor.execute("SELECT * FROM PROFILE")
#
# pro = Profile()
# roww = cursor.fetchone()
# pro.phone(roww)

# cursor.execute(''' CREATE TABLE PROFILE (ID Student TEXT, Name Student TEXT,
#                 Date of birth TEXT, Brithplace TEXT, Nationality TEXT, Education TEXT,
#                 Disease TEXT, Relative TEXT, Phone TEXT, Address TEXT, Email TEXT)''')
#
# cursor.execute("""insert into PROFILE values('59340500021', 'Thipawan', '14/02/40', 'thailand', 'thai',
# 'Bachelor', 'None', 'single', '094-2690207', 'Bangkok', 'thipa@gmail.com')""")
# conne.commit()

# conne = sqlite3.connect("Profiledata.db")
# conne.row_factory = sqlite3.Row
# cursor = conne.cursor()
# cursor.execute("SELECT * FROM PROFILE")
#
# pro = Profile()
# roww = cursor.fetchone()
# pro.phone(roww)
