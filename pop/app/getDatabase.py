import os
import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from databaseSetup import *

engine = create_engine('sqlite:///Database.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
query = session.query(Profile)
Acque = session.query(Activity)
disquery = session.query(Disease)

class return_Method:

    def __init__(self,data):
        self.data = data

    def name(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Name

    def surname(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Surname

    def sex(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Sex

    def year(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Year

    def date(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Dateofbirth

    def birth(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Birthplace

    def nation(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Nationality

    def education(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Education

    def disease(self):
        box = []
        for user in disquery.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Disease)
        return box

    def relative(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return  user.Relative

    def PhoneEmer(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.PhoneforEmergency

    def Phonestu(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Phonestudent

    def address(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Address

    def email(self):
        for user in query.filter_by(id_student = "{}".format(self.data)):
            return user.Email

    def Act_name(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.NameActivity)
        return box

    def Act_des(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Description)
        return box

    def Act_photo(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Photo)
        return box

    def Act_type(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Type)
        return box

    def Act_advisor(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Advisor)
        return box

    def Act_Date(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Date_Activity)
        return box

    def Act_file(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.File)
        return box

    def Act_confirm(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Confirm)
        return box

class return_data(return_Method):

    # def Dicdisease(self,Disease = None):
    #     dataAct = []
    #     for item in Disease:
    #         dicAct = {'id_student' : self.data, 'Disease ' : item}
    #         dataAct.append(dicAct)
    #     return dataAct

    def DicPro(self,name = None, surname = None, date = None, birth = None, nation = None, edu = None, disease = None, relative = None, phoneEmer = None, phonestu = None, address = None, email = None ):
        dataPro = []
        x = ",".join(disease)
        dicPro = {'Name' : name, 'Surname' : surname, 'Dateofbirth' : date, 'Birthplace' : birth, 'Nation' : nation,
                'Education' : edu,  'Disease' : x, 'Relative' : relative,'PhoneEmer' : phoneEmer, 'Phonestudent' : phonestu, 'Address' : address, 'Email' : email }
        dataPro.append(dicPro)
        return dataPro

    def DicAct(self,NameAct = None, Descrip = None, Photo = None, Type = None, Advisor = None, Date = None, File = None, Confirm = None ):
        dataAct = []
        for item in range(len(NameAct)):
            dicAct = {'Name Activity' : NameAct[item], 'Description' : Descrip[item], 'Photo' : Photo[item], 'Type' : Type[item], 'Advisor' : Advisor[item], 'Date_Activity' : Date[item], 'File' : File[item], 'Confirm' : Confirm[item]}
            dataAct.append(dicAct)
        return dataAct

class Get_Academic:
    def __init__(self,studenID,term):
        self.studenID = studenID
        self.term = term
    def get_id_subject(self):
        query = session.query(Academic)
        list_idSub = []
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            list_idSub.append(i.ID_Subject)
        return list_idSub

    def get_grade(self):
        query = session.query(Academic)
        list_grade = []
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            list_grade.append(i.Grade)
        return list_grade
    # print(get_grade())

    def get_this_semester_credit(self):
        termCredit = []
        query = session.query(Gpa)
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            termCredit.append(i.sum_credit)
        return termCredit
    # print(get_this_semester_credit())

    def get_cumulative_credit(self):
        allCredit = []
        query = session.query(Gpax)
        for i in query.filter_by(Student_ID="{}".format(self.studenID)):
            allCredit.append(i.sum_all_credit)
        return allCredit
    # print(get_cumulative_credit())

    def get_GPA(self):
        gpa = []
        query = session.query(Gpa)
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            gpa.append(i.GPA)
        return gpa
    # print(get_GPA())

    def get_GPAX(self):
        gpax = []
        query = session.query(Gpax)
        for i in query.filter_by(Student_ID="{}".format(self.studenID)):
            gpax.append(i.GPAX)
        return gpax
    # print(get_GPAX())

class Get_name_credit_subject:
    def __init__(self,studenID,term):
        self.studenID = studenID
        self.term = term
    def get_nameSubject(self):

        query = session.query(Subject)
        a = Get_Academic.get_id_subject(self)
        b = []
        for i in a:
            for j in query.filter_by(ID_Subject="{}".format(i)):
                b.append(j.name_subject)
        return b

    def get_credit(self):
        query = session.query(Subject)
        c = Get_Academic.get_id_subject(self)
        d = []
        for i in c:
            for j in query.filter_by(ID_Subject="{}".format(i)):
                d.append(j.Credit)
        return d
    # print(get_credit())

class Academic_1st_table:
    def output_term(self,idsub = None,namesub = None,credit = None,grade = None):
        list_output_term = []
        for i in range(len(idsub)):
            dict_output_term = {"ID_Subject":idsub[i],"Name_Subject":namesub[i],
             "Credit":credit[i],"Academic_Regcord":grade[i]}
            list_output_term.append(dict_output_term)
        return list_output_term

class Academic_2st_table:
    def output_sum(self,this_credit = None,gpa = None,cumulative_credit = None,gpax = None):
        list_sum_output = []
        for i in range(len(cumulative_credit)):
            dict_output_term = {"This_semester":this_credit[i],"GPA":gpa[i],
             "Cumulative_credit":cumulative_credit[i],"GPAX":gpax[i]}
            list_sum_output.append(dict_output_term)
        return list_sum_output
