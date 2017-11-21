import os
import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from databaseSetup import *
import collections

engine = create_engine('sqlite:///Database.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
query = session.query(Profile)
Acque = session.query(Activity)
disquery = session.query(Disease)
teacher = session.query(TeacherPW)

class return_Method:

    def __init__(self,data):
        self.data = data

    def idstu(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.id_student

    def name(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Name

    def surname(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Surname

    def sex(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Sex

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

    def photo(self):
        for user in query.filter_by(id_student = "{}".format(self.data)):
            return user.Photo

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

    def t_name(self):
        for user in teacher.filter_by(id_teacher="{}".format(self.data)):
            return user.Name

    def t_surname(self):
        for user in teacher.filter_by(id_teacher="{}".format(self.data)):
            return user.Surname


class return_data(return_Method):

    def DicPro(self,name = None, surname = None, date = None, birth = None, nation = None, edu = None, disease = None, relative = None, phoneEmer = None, phonestu = None, address = None, email = None, photo = None ):
        dataPro = []
        Newdisease = ",".join(disease)
        dicPro = {'Name' : name, 'Surname' : surname, 'Dateofbirth' : date, 'Birthplace' : birth, 'Nation' : nation,
                'Education' : edu,  'Disease' : Newdisease, 'Relative' : relative,'PhoneEmer' : phoneEmer, 'Phonestudent' : phonestu, 'Address' : address, 'Email' : email, 'Photo' : photo }
        dataPro.append(dicPro)
        return dataPro

    def DicAct(self,NameAct = None, Descrip = None, Photo = None, Type = None, Advisor = None, Date = None, File = None, Confirm = None ):
        dataAct = []
        for item in range(len(NameAct)):
            dicAct = {'Name_Activity' : NameAct[item], 'Description' : Descrip[item], 'Photo' : Photo[item], 'Type' : Type[item], 'Advisor' : Advisor[item], 'Date_Activity' : Date[item], 'File' : File[item], 'Confirm' : Confirm[item]}
            dataAct.append(dicAct)
        return dataAct

    def DicFRAB(self):
        box = []
        for instance in session.query(Profile).order_by(Profile.id_student):
            id = instance.id_student
            box.append(id)
        countid = [item for item, count in collections.Counter(box).items() if count >= 1]
        Frab = [i for i in countid if str(i)[:2] == "59"]
        return Frab


class Edit:
    def __init__(self,id):
        self.id = id

    def edit_disease(self,edit,data):
        for item in edit:
            spinach = session.query(Disease).filter_by(id_student = "{}".format(self.id),Disease = "{}".format(item)).one()
            session.delete(spinach)
        sth = Disease(id_student = "{}".format(self.id),Disease = "{}".format(data))
        session.add(sth)
        session.commit()

    def deleteAct(self,name): # delete function
        spinach = session.query(Activity).filter_by(id_student = "{}".format(self.id), NameActivity = "{}".format(name)).one()
        session.delete(spinach)
        session.commit()

class Add_Method:

    def __init__(self,id):
        self.id = id

    def id_stu(self,method):
        sth = method(id_student = "{}".format(self.id))
        session.add(sth)
        session.commit()

    def name(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Name = "{}".format(data)
        session.add(addData)
        session.commit()

    def Surname(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Surname = "{}".format(data)
        session.add(addData)
        session.commit()

    def date(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Dateofbirth = "{}".format(data)
        session.add(addData)
        session.commit()

    def birth(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Birthplace = "{}".format(data)
        session.add(addData)
        session.commit()

    def nation(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Nationality = "{}".format(data)
        session.add(addData)
        session.commit()

    def education(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Education = "{}".format(data)
        session.add(addData)
        session.commit()

    def disease(self,data):
        sth = Disease(id_student = "{}".format(self.id),Disease = "{}".format(data))
        session.add(sth)
        session.commit()

    def relative(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Relative = "{}".format(data)
        session.add(addData)
        session.commit()

    def phoneEmer(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.PhoneforEmergency = "{}".format(data)
        session.add(addData)
        session.commit()

    def phonestu(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Phonestudent = "{}".format(data)
        session.add(addData)
        session.commit()

    def address(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Address = "{}".format(data)
        session.add(addData)
        session.commit()

    def email(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Email = "{}".format(data)
        session.add(addData)
        session.commit()

    def photo(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Photo = "{}".format(data)
        session.add(addData)
        session.commit()

    def Act_name(self,nameAct):
        sth = Activity(id_student = "{}".format(self.id),NameActivity = "{}".format(nameAct))
        session.add(sth)
        session.commit()

    def Act_des(self,data,nameAct):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id),NameActivity = "{}".format(nameAct)).one()
        addData.Description = "{}".format(data)
        session.add(addData)
        session.commit()

    def Act_photo(self,data,nameAct):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id),NameActivity = "{}".format(nameAct)).one()
        addData.Photo = "{}".format(data)
        session.add(addData)
        session.commit()

    def Act_type(self,data,nameAct):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id),NameActivity = "{}".format(nameAct)).one()
        addData.Type = "{}".format(data)
        session.add(addData)
        session.commit()

    def Act_advisor(self,data,nameAct):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id),NameActivity = "{}".format(nameAct)).one()
        addData.Advisor = "{}".format(data)
        session.add(addData)
        session.commit()

    def Act_date(self,data,nameAct):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id),NameActivity = "{}".format(nameAct)).one()
        addData.Date_Activity = "{}".format(data)
        session.add(addData)
        session.commit()

    def Act_file(self,data,nameAct):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id),NameActivity = "{}".format(nameAct)).one()
        addData.File = "{}".format(data)
        session.add(addData)
        session.commit()

    def Act_confirm(self,data,nameAct):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id),NameActivity = "{}".format(nameAct)).one()
        addData.Confirm = "{}".format(data)
        session.add(addData)
        session.commit()

    def Academic_Gpax(self,data):
        addData = session.query(Gpax).filter_by(Student_ID="{}".format(self.id)).one()
        addData.GPAX = "{}".format(data)
        session.add(addData)
        session.commit()

    def Academic_sum_credit(self,data):
        addData = session.query(Gpax).filter_by(Student_ID="{}".format(self.id)).one()
        addData.sum_all_credit = "{}".format(data)
        session.add(addData)
        session.commit()

    def subject_credit(self,ID_Sub,data):
        addData = session.query(Subject).filter_by(ID_Subject="{}".format(ID_Sub)).one()
        addData.Credit = "{}".format(data)
        session.add(addData)
        session.commit()

    def Dicdisease(self,Disease = None):
        dataAct = []
        for item in Disease:
            dicAct = {'id_student' : self.id, 'Disease ' : item}
            dataAct.append(dicAct)
        return dataAct
#############################################################
    def edit_disease(self,edit,data):
        print(edit)
        for item in edit:
            spinach = session.query(Disease).filter_by(id_student = "{}".format(self.id),Disease = "{}".format(item)).one()
            session.delete(spinach)
            print(item)
        sth = Disease(id_student = "{}".format(self.id),Disease = "{}".format(data))
        session.add(sth)
        session.commit()


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

class Check:
        def T_check(self,ID,password):
            box_id = []
            box_P = []
            for instance in session.query(TeacherPW).order_by(TeacherPW.id_teacher):
                x = instance.id_teacher
                box_id.append(x)

            for instance in session.query(TeacherPW).order_by(TeacherPW.T_Password):
                x = instance.T_Password
                box_P.append(x)
            count = 0
            print (box_id)
            for i in box_id:
                if i == ID:
                    count += 1
            #print(count)
            #print(box_P)
            for j in box_P:
                if j == password:
                    count += 1
            #print(count)
            if count == 2:
                print("True")
                return True
            else:
                print("False")
                return False

        def S_check(self,ID,password):
            #print(ID)
            #print(password)
            box_id = []
            box_P = []
            for instance in session.query(StudentPW).order_by(StudentPW.id_student):
                x = instance.id_student
                box_id.append(x)

            for instance in session.query(StudentPW).order_by(StudentPW.S_Password):
                x = instance.S_Password
                box_P.append(x)

            count = 0
            #print (box_id)
            for i in box_id:
                if i == ID:
                    count += 1
                    #print (count)
            #print (box_P)
            for j in box_P:
                if j == password :
                    count += 1
                    #print (count)
            #print (count)
            if count == 2 :
                print("True")
                return True
            else:
                print("False")
                return False


        def FRAB(self,frab):
            year = 56 + int(frab)
            id_stu = []
            datafrab = []
            for instance in session.query(Profile).order_by(Profile.id_student):
                x = instance.id_student
                id_stu.append(x)
            id = [item for item, count in collections.Counter(id_stu).items() if count == 1]
            include = [i for i in id if str(i)[:2] == str(year)]
            for item in include:
                re = return_Method(item)
                dicfrab = {'Name' : re.name(),'Surname' : re.surname(),'ID' : re.idstu()}
                datafrab.append(dicfrab)
            return datafrab

        def checkfrab(self):
            box = []
            include = []
            for instance in session.query(Profile).order_by(Profile.id_student):
                x = instance.id_student
                box.append(str(x))
            for i in box:
                year = str(i)[:2]
                frab = int(year) - 56
                word = "FRAB#"+str(frab)
                if word not in include:
                    include.append(word)
            return include

        def TERM(self,studentID):
            query = session.query(Academic)
            list_idSub = []
            box = []
            for instance in query.filter_by(Student_ID="{}".format(studentID)):
                list_idSub.append(instance.Term)
            for item in list_idSub:
                if item not in box:
                    box.append(item)
            return box

        def all_student(self):
            student = []
            for m in session.query(*Profile.__table__.columns).all():
                student.append(str(m[0]))
            return student

        def gpax_student_id(self,studentID):
            query = session.query(Gpax)
            list_idstudent = []
            for i in query.filter_by(Student_ID="{}".format(studentID)):
                if str(i.Student_ID) == str(studentID):
                    return True
            else:
                return False
