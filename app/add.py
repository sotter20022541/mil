from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseSetup import *

engine = create_engine('sqlite:///Database.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#----------------------------add subject---------------------------------------#
sub = Subject(ID_Subject ="FRA141",name_subject ="COMPUTER PROGRAMMING")
session.add(sub)
sub = Subject(ID_Subject ="FRA161",name_subject ="ROBOTICS EXPLORATION")
session.add(sub)
sub = Subject(ID_Subject ="GEN101",name_subject ="PHYSICAL EDUCATION")
session.add(sub)
sub = Subject(ID_Subject ="LNG101",name_subject ="GENERAL ENGLISH")
session.add(sub)
sub = Subject(ID_Subject ="LNG102",name_subject ="TECHNICAL ENGLISH")
session.add(sub)
sub = Subject(ID_Subject ="MTH101",name_subject ="MATHEMATICS I")
session.add(sub)
sub = Subject(ID_Subject ="PHY103",name_subject ="GENERAL PHYSICS")
session.add(sub)
sub = Subject(ID_Subject ="PHY191",name_subject ="GENERAL PHYSICS LABORATORY I")
session.add(sub)
sub = Subject(ID_Subject ="FRA121",name_subject ="ELECTRONIC CIRCUITS")
session.add(sub)
sub = Subject(ID_Subject ="FRA142",name_subject ="COMPUTER PROGRAMMING")
session.add(sub)
sub = Subject(ID_Subject ="FRA162",name_subject ="ROBOTICS AND AUTOMATION")
session.add(sub)
sub = Subject(ID_Subject ="FRA163",name_subject ="ROBOTICS MACHINE SHOP")
session.add(sub)
sub = Subject(ID_Subject ="GEN111",name_subject ="MAN AND ETHICS OF LIVING")
session.add(sub)
sub = Subject(ID_Subject ="GEN121",name_subject ="LEARNING AND PROBLEM SOLVING SKILLS")
session.add(sub)
sub = Subject(ID_Subject ="MTH102",name_subject ="MATHEMATICS II")
session.add(sub)
sub = Subject(ID_Subject ="FRA221",name_subject ="DIGITAL ELECTRONICS")
session.add(sub)
sub = Subject(ID_Subject ="FRA222",name_subject ="INDUSTRIAL SENSORSAND ACTUATORS")
session.add(sub)
sub = Subject(ID_Subject ="FRA231",name_subject ="STATICS AND DYNAMICS")
session.add(sub)
sub = Subject(ID_Subject ="FRA241",name_subject ="SOFTWARE DEVELOPMENT FOR ROBOTICS AND AUTOMATION ENGINEERING")
session.add(sub)
sub = Subject(ID_Subject ="FRA261",name_subject ="ROBOTICSAND AUTOMATION ENGINEERING LAB II")
session.add(sub)
sub = Subject(ID_Subject ="LNG103",name_subject ="ENGLISH FOR WORKPLACE COMMUNICATION")
session.add(sub)
sub = Subject(ID_Subject ="MTH201",name_subject ="MATHEMATICS III")
session.add(sub)
sub = Subject(ID_Subject ="FRA223",name_subject ="EXPLORATION IN SIGNALS AND SYSTEMS")
session.add(sub)
sub = Subject(ID_Subject ="FRA232",name_subject ="ROBOT STRUCTURE DESIGN I")
session.add(sub)
sub = Subject(ID_Subject ="FRA262",name_subject ="INVENTOR STUDIO")
session.add(sub)
sub = Subject(ID_Subject ="GEN231",name_subject ="MIRACLE OF THINKING")
session.add(sub)
sub = Subject(ID_Subject ="GEN241",name_subject ="BEAUTY OF LIFE")
session.add(sub)
sub = Subject(ID_Subject ="STA302",name_subject ="STATISTICS FOR ENGINEERS")
session.add(sub)
sub = Subject(ID_Subject ="FRA321",name_subject ="IMAGE PROCESSING AND ANALYSIS")
session.add(sub)
sub = Subject(ID_Subject ="FRA331",name_subject ="BASIC CONTROL THEORY")
session.add(sub)
sub = Subject(ID_Subject ="FRA332",name_subject ="ROBOT STRUCTURE DESIGN II")
session.add(sub)
sub = Subject(ID_Subject ="FRA341",name_subject ="EMBEDDED SYSTEM DESIGN")
session.add(sub)
sub = Subject(ID_Subject ="FRA361",name_subject ="ROBOTICS AND AUTOMATION ENGINEERING LAB III")
session.add(sub)
sub = Subject(ID_Subject ="GEN211",name_subject ="THE PHILOSOPHY OF SUFFICIENCY ECONOMY")
session.add(sub)
sub = Subject(ID_Subject ="GEN212",name_subject ="MIND DEVELOPMENT THROUGH BUDDHISM FOR A FULFILLING LIFE")
session.add(sub)
sub = Subject(ID_Subject ="GEN301",name_subject ="HOLISTIC HEALTH DEVELOPMENT")
session.add(sub)
sub = Subject(ID_Subject ="GEN311",name_subject ="ETHICS IN SCIENCE-BASED SOCIETY")
session.add(sub)
sub = Subject(ID_Subject ="GEN321",name_subject ="THE HISTORY OF CIVILIZATION")
session.add(sub)
sub = Subject(ID_Subject ="GEN331",name_subject ="MAN AND REASONING")
session.add(sub)
sub = Subject(ID_Subject ="GEN341",name_subject ="THAI INDIGENOUS KNOWLEDGE")
session.add(sub)
sub = Subject(ID_Subject ="GEN352",name_subject ="TECHNOLOGY AND INNOVATION FOR SUSTAINABLE DEVELOPMENT")
session.add(sub)
sub = Subject(ID_Subject ="GEN353",name_subject ="MANAGERIAL PSYCHOLOGY")
session.add(sub)
sub = Subject(ID_Subject ="GEN411",name_subject ="PERSONALITY DEVELOPMENT AND PUBLIC SPEAKING")
session.add(sub)
sub = Subject(ID_Subject ="GEN412",name_subject ="SCIENCE AND ART OF LIVING AND WORKING")
session.add(sub)
sub = Subject(ID_Subject ="GEN421",name_subject ="INTEGRATIVE SOCIAL SCIENCES")
session.add(sub)
sub = Subject(ID_Subject ="GEN441",name_subject ="CULTURE AND EXCURSION")
session.add(sub)
sub = Subject(ID_Subject ="FRA300",name_subject ="INDUSTRIAL TRAINING")
session.add(sub)
sub = Subject(ID_Subject ="FRA311",name_subject ="ARTIFICIAL INTELLIGENCE FOR ROBOTICS AND AUTOMATION ENGINEERING")
session.add(sub)
sub = Subject(ID_Subject ="FRA333",name_subject ="INTRODUCTION TO ROBOTICS")
session.add(sub)
sub = Subject(ID_Subject ="FRA351",name_subject ="COMPUTERAIDED TECHNOLOGIES")
session.add(sub)
sub = Subject(ID_Subject ="FRA362",name_subject ="ROBOTICS STUDIO")
session.add(sub)
sub = Subject(ID_Subject ="GEN351",name_subject ="MODERN MANAGEMENT AND LEADERSHIP")
session.add(sub)

# session.commit()
# -------------------------------------------------------------------#

sth = Profile(id_student = 59340500035,Name = "Panchalee",Surname  = "Sookprao", Sex = "Miss",Dateofbirth = "12/21/41",Birthplace = "Hospital",Nationality = "Thai",Education = "Surin",Relative = "mom",PhoneforEmergency = "3434343434",Phonestudent = "66666666" ,Address = "Surin",Email = "pop@gmail.com",Photo = "59340500035.jpg")
sth1 = Profile(id_student = 59340500021,Name = "Thipawan",Surname  = "Pairam", Sex = "Miss",Dateofbirth = "14/09/40",Birthplace = "Hospital1",Nationality = "Thai",Education = "Bungkan",Relative = "Dad",PhoneforEmergency = "0941234567",Phonestudent = "0867654321" ,Address = "Bungkan",Email = "pair@gmail.com",Photo = "59340500021.jpg")
sth2 = Profile(id_student = 59340500017,Name = "Natthaphon",Surname  = "Sudadech", Sex = "Mr", Dateofbirth = "05/03/39",Birthplace = "Hospital2",Nationality = "Thai",Education = "Bungkan",Relative = "Mom",PhoneforEmergency = "087654321",Phonestudent = "0865432111" ,Address = "Bungkan",Email = "mill@gmail.com",Photo = "59340500017.jpg")
sth3 = Profile(id_student = 58340500011,Name = "Chanittha",Surname  = "Techasombooranakit", Sex = "Miss", Dateofbirth = "11/10/39",Birthplace = "Hospital3",Nationality = "Thai",Education = "Banakok",Relative = "Dad",PhoneforEmergency = "067894332",Phonestudent = "087625434" ,Address = "Bangkok",Email = "winnie@gmail.com",Photo = "58340500011.jpg")
sth4 = Profile(id_student = 58340500014,Name = "Chawisorn",Surname  = "Samrit", Sex = "Mr", Dateofbirth = "21/01/39",Birthplace = "Hospital4",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "09999999999",Phonestudent = "08799999" ,Address = "Bangkok",Email = "green@gmail.com",Photo = "58340500014.jpg")
sth5 = Profile(id_student = 57340500008,Name = "Chakputtana",Surname  = "Sangpradit", Sex = "Miss", Dateofbirth = "24/05/38",Birthplace = "Hospital5",Nationality = "Thai",Education = "Saraburi",Relative = "Dad",PhoneforEmergency = "0891111111",Phonestudent = "0871111111" ,Address = "Bangkok",Email = "sod@gmail.com",Photo = "57340500008.jpg")
sth6 = Profile(id_student = 57340500016,Name = "Nuttida",Surname  = "Peeklom", Sex = "Miss", Dateofbirth = "12/06/38",Birthplace = "Hospital6",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "0812222222",Phonestudent = "078888888" ,Address = "Bangkok",Email = "tan@gmail.com",Photo = "57340500016.jpg")
sth7 = Profile(id_student = 60340500004,Name = "Kelwalee",Surname  = "rattanasakulthong", Sex = "Miss", Dateofbirth = "19/08/41",Birthplace = "Hospital7",Nationality = "Thai",Education = "Banakok",Relative = "Dad",PhoneforEmergency = "0934444444",Phonestudent = "0954444444" ,Address = "Bangkok",Email = "kel@gmail.com",Photo = "60340500004.jpg")
sth8 = Profile(id_student = 60340500050,Name = "Lanna",Surname  = "Foolek", Sex = "Miss", Dateofbirth = "30/05/41",Birthplace = "Hospital8",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "0941111111",Phonestudent = "061111111" ,Address = "Bangkok",Email = "mai@gmail.com",Photo = "60340500050.jpg")

session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.
session.add(sth3) #add sth into database.
session.add(sth4) #add sth into database.
session.add(sth5) #add sth into database.
session.add(sth6) #add sth into database.
session.add(sth7) #add sth into database.
session.add(sth8) #add sth into database.
sth = Activity(id_student = 59340500017,NameActivity = "Natthaphon",Description = "this is so fun.",Photo = "Natthaphon.jpg",Type = "Dynamics",Advisor = "AJ.Ton",Date_Activity = "14/12/60",File = "file of the Activity.",Confirm = "Not Confirm yet")
sth1 = Activity(id_student = 59340500021,NameActivity = "Thipawan",Description = "Receive a lot of knowledges.",Photo = "Thipawan.jpg",Type = "Calculas",Advisor = "AJ.Somran",Date_Activity = "15/12/61",File = "file of the Activity1.",Confirm = "Confirm")
sth2 = Activity(id_student = 59340500035,NameActivity = "Panchalee",Description = "It is will be useful.",Photo = "Panchalee.jpg",Type = "Digital",Advisor = "AJ.Pi",Date_Activity = "15/12/60",File = "file of the Activity2.",Confirm = "Confirm")
sth3 = Activity(id_student = 59340500035,NameActivity = "Tabletennnis",Description = "Table tennis is good.",Photo = "Tabletennnis.jpg",Type = "Sport",Advisor = "AJ.__",Date_Activity = "29/05/60",File = "file of the Activity3.",Confirm = "Confirm")
sth4 = Activity(id_student = 58340500011,NameActivity = "Project",Description = "This project is very hard.",Photo = "Project.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "19/10/61",File = "file of the Activity4.",Confirm = "Not Confirm yet")
sth5 = Activity(id_student = 57340500008,NameActivity = "FootballKMUTT",Description = "This is my favorite sport.",Photo = "FootballKMUTT.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "20/10/61",File = "file of the Activity5.",Confirm = "Confirm ")
sth6 = Activity(id_student = 57340500016,NameActivity = "Chorus",Description = "This is my favorite hobbit.",Photo = "Chorus.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "21/10/61",File = "file of the Activity6.",Confirm = "Not Confirm yet")
sth7 = Activity(id_student = 58340500014,NameActivity = "SuperRobot",Description = "This is my favorite hobbit.",Photo = "SuperRobot.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "22/10/61",File = "file of the Activity7.",Confirm = "Not Confirm yet")
sth8 = Activity(id_student = 60340500004,NameActivity = "CatRobot",Description = "This is my favorite animal.",Photo = "CatRobot.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "23/10/61",File = "file of the Dynamic8.",Confirm = "Confirm")
sth9 = Activity(id_student = 60340500050,NameActivity = "DesignUI",Description = "This is my favorite work.",Photo = "DesignUI.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "24/10/61",File = "file of the Activity9.",Confirm = "Not Confirm yet")

session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.
session.add(sth3) #add sth into database.
session.add(sth4) #add sth into database.
session.add(sth5) #add sth into database.
session.add(sth6) #add sth into database.
session.add(sth7) #add sth into database.
session.add(sth8) #add sth into database.
session.add(sth9) #add sth into database.


sth = Disease(id_student = 59340500017,Disease = "gout")
sth1 = Disease(id_student = 59340500017,Disease = "hemorrhoids")
sth2 = Disease(id_student = 59340500017,Disease = "pneumonia")
sth3 = Disease(id_student = 58340500011,Disease = "headache")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.
session.add(sth3) #add sth into database.

sth = Disease(id_student = 59340500035,Disease = "diarrhea")
sth1 = Disease(id_student = 59340500035,Disease = "enteritis")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.

sth = Disease(id_student = 59340500021,Disease = "heart disease")
sth1 = Disease(id_student = 59340500021,Disease = "measles")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
# session.commit() #commit data that increase.

sth = Disease(id_student = 57340500008,Disease = "sick4")
sth1 = Disease(id_student = 57340500016,Disease = "sick3")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
# session.commit() #commit data that increase.

sth = Disease(id_student = 58340500014,Disease = "sick2")
sth1 = Disease(id_student = 60340500004,Disease = "sick1")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
# session.commit() #commit data that increase.

sth = Disease(id_student = 60340500050,Disease = "sick")
session.add(sth) #add sth into database.
# session.commit() #commit data that increase.

sth = TeacherPW(id_teacher = 100 ,Name = "Warasinee", Surname = "Chaisangmongkon",T_Password = "100")
sth1 = TeacherPW(id_teacher = 200 ,Name = "Bawornsak", Surname = "Sakulkueakulsuk",T_Password = "200")
sth2 = TeacherPW(id_teacher = 300 ,Name = "Suriya", Surname = "Natsupakpong",T_Password = "300")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.

sth = StudentPW(id_student = 59340500021,S_Password = "59340500021")
sth1 = StudentPW(id_student = 59340500035,S_Password = "59340500035")
sth2 = StudentPW(id_student = 59340500017,S_Password = "59340500017")
sth3 = StudentPW(id_student = 58340500011,S_Password = "58340500011")
sth4 = StudentPW(id_student = 58340500014,S_Password = "58340500014")
sth5 = StudentPW(id_student = 57340500008,S_Password = "57340500008")
sth6 = StudentPW(id_student = 57340500016,S_Password = "57340500016")
sth7 = StudentPW(id_student = 60340500004,S_Password = "57340500004")
sth8 = StudentPW(id_student = 60340500050,S_Password = "57340500050")
session.add(sth)
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.
session.add(sth3) #add sth into database.
session.add(sth4) #add sth into database.
session.add(sth5) #add sth into database.
session.add(sth6) #add sth into database.
session.add(sth7) #add sth into database.
session.add(sth8) #add sth into database.
session.commit() #commit data that increase.
