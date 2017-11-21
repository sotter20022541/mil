import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseSetup import *
from getDatabase import *

engine = create_engine('sqlite:///Database.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

class Input_Academics:
    def __init__(self,path,interm):
        self.path = path
        self.term = interm

    def input_Academic_and_edit_data(self):
#---------------------------want from input---------------------------#
        grade_file = self.path
        df = pd.read_csv(grade_file,sep=',')
        input_term = self.term

########################################################
        row = len(df.index)
        column = len(df.columns)
        g = df.head(row)

########################################################
        all_student_ID = g["name subject"]
        list_all_student = []
        count_student = 2
        while(count_student < row):
            student = all_student_ID[count_student]
            list_all_student.append(student)
            count_student+=1
        # print(list_all_student)

        list_True_student = []
        check = Check()
        # print(check.all_student())
        for u in check.all_student():
            for v in list_all_student:
                if u == v:
                    list_True_student.append(v)
        # print("list_True_student = ",list_True_student)
        list_False_student = list(set(list_all_student) - set(list_True_student))
        # print("list_False_student = ",list_False_student)

        # print(row)

################################################################
        count_row = 2
        while(count_row < row - len(list_False_student)):
            student_ID = all_student_ID[count_row]
            # print(student_ID)

            if str(student_ID) in list_True_student:
                # print("loop id = ",student_ID)

                add = Add_Method(student_ID)
                o = Academic_1st_table()
                grade = df.loc[df['name subject'] == student_ID]
                list_sub = []
                list_grade = []
                list_credit = []
                list_credits = []
                for name_subject in grade:
                    g = grade[name_subject]
                    h = str(g[count_row])
                    if h != "nan":
                        # print(name_subject)
                        list_sub.append(name_subject)
                        # print(name_subject)                          #name Sub
                        list_grade.append(float(grade[name_subject]))
                        # print(float(grade[name_subject]))              #grade


                # count_row += 1
                del list_sub[0]
                del list_grade[0]
                cre = df.loc[df['name subject'] == "credit"]
                for j in list_sub:
                    s = cre[j]
                    list_credit.append(s[0])

                for k in list_credit:
                    list_credits.append(float(k))
                term_credit = sum(list_credits)
########################################################################
                for sub,cr in zip(list_sub,list_credits):
                    add.subject_credit(sub,cr)

#######################################################################
                list_c = []
                for gg, cc in zip(list_grade, list_credits):
                    ss = gg*cc
                    list_c.append(ss)
                gpa = sum(list_c) / term_credit
                GPA = '%.2f' %gpa
                # print(len(list_sub))
#####################################################################
                count_column = 0
                while(count_column < len(list_sub)):
                    student = Academic(Student_ID = int(student_ID),Term = str(input_term),
                     ID_Subject = str(list_sub[count_column]),Grade = str(list_grade[count_column]) )
                    session.add(student)
                    count_column += 1
                gpa = Gpa(Student_ID = int(student_ID),Term = str(input_term),
                sum_credit = int(term_credit),GPA = GPA)
                session.add(gpa)
#########################################################################
                check = Check()
                ckeck_id = check.gpax_student_id(student_ID)
                if ckeck_id == False:
                    gx = Gpax(Student_ID = int(student_ID))
                    session.add(gx)
#########################################################################
                session.commit()
#########################################################################
                check = Check()
                List_term = check.TERM(student_ID)
                list_mul = []
                list_sum_credit = []
                for p in List_term:
                    s = Get_Academic(student_ID,p)
                    t = Get_name_credit_subject(student_ID,p)
                    w = o.output_term(s.get_id_subject(),t.get_nameSubject(),t.get_credit(),s.get_grade())
                    for i in w:
                        list_sum_credit.append(float(i["Credit"]))
                        d = float(i["Credit"]) * float(i["Academic_Regcord"])
                        list_mul.append(d)
                sum_list_sum_credit = sum(list_sum_credit)
                sum_list_mul = sum(list_mul)
                gpax = sum_list_mul / sum_list_sum_credit
                GPAX = '%.2f' %gpax
                add.Academic_Gpax(str(GPAX))
                add.Academic_sum_credit(str(sum_list_sum_credit))

            count_row += 1
            self.Other_student = list_False_student
        # return list_False_student

    def other_student(self):
        return self.Other_student
