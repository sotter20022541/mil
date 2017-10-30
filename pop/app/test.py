from getDatabase import *
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
print(p.output_sum(s.get_this_semester_credit(),s.get_GPA(),s.get_cumulative_credit(),s.get_GPAX()))
