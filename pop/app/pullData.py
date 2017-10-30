from getDatabase import *
''''
studenID = "59340500021"
term = "1/2559"


s = Get_Academic(studenID,term)
t = Get_name_credit_subject(studenID,term)
o = Academic_1st_table()
p = Academic_2st_table()
re = return_Method(studenID)
returnda = return_data(studenID)

print("Profile: ")
print(returnda.DicPro(re.name(), re.surname(), re.date(), re.birth(), re.nation(), re.education(), re.disease(), re.PhoneEmer(), re.Phonestu(), re.address(), re.email()))
print("Activity: ")
print(returnda.DicAct(re.Act_name(), re.Act_des(), re.Act_photo(), re.Act_type(), re.Act_advisor(), re.Act_Date(), re.Act_file(), re.Act_confirm()))
print("output_term: ")
print(o.output_term(s.get_id_subject(),t.get_nameSubject(),t.get_credit(),s.get_grade()))
print("output_sum: ")
print(p.output_sum(s.get_this_semester_credit(),s.get_GPA(),s.get_cumulative_credit(),s.get_GPAX())) '''


class pullData():

    def __init__(self, profile=None, academicTerm =None, activity=None ,academicSum=None, academic =None):
        self.profile = profile
        self.academicTerm = academicTerm
        self.activity = activity
        self.academicSum = academicSum
        self.academic = academic

    def Profile(self, getID):
        re = return_Method(getID)
        returnda = return_data(getID)
        self.profile = returnda.DicPro(re.name(), re.surname(), re.date(), re.birth(), re.nation(), re.education(), re.disease(), re.relative(), re.PhoneEmer(), re.Phonestu(), re.address(), re.email())
        return self.profile

    def Activity(self, getID):
        re = return_Method(getID)
        returnda = return_data(getID)
        self.activity = returnda.DicAct(re.Act_name(), re.Act_des(), re.Act_photo(), re.Act_type(), re.Act_advisor(), re.Act_Date(), re.Act_file(), re.Act_confirm())
        return self.activity

    def Academic_term(self, getID, term = None):
        if term == None:
            A = [{"ID_Subject":None,"Name_Subject":None,"Credit":None,"Academic_Regcord":None}]
            return A
        else:
            s = Get_Academic(getID,term)
            t = Get_name_credit_subject(getID,term)
            o = Academic_1st_table()
            p = Academic_2st_table()
            self.academicTerm = o.output_term(s.get_id_subject(),t.get_nameSubject(),t.get_credit(),s.get_grade())
            return self.academicTerm


    def Academic_sum(self, getID, term = None):
        if term == None:
            A =[{"This_semester":None,"GPA":None,"Cumulative_credit":None,"GPAX":None}]
            return A
        else :
            s = Get_Academic(getID,term)
            t = Get_name_credit_subject(getID,term)
            o = Academic_1st_table()
            p = Academic_2st_table()
            self.academicSum = p.output_sum(s.get_this_semester_credit(),s.get_GPA(),s.get_cumulative_credit(),s.get_GPAX())
            return self.academicSum
