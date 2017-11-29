from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseSetup import *

engine = create_engine('sqlite:///Database.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# #----------------------------add subject---------------------------------------#
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

# sth = Profile(id_student = 59340500035,Name = "Panchalee",Surname  = "Sookprao", Sex = "Miss",Dateofbirth = "12/21/41",Birthplace = "Hospital",Nationality = "Thai",Education = "Surin",Relative = "mom",PhoneforEmergency = "3434343434",Phonestudent = "66666666" ,Address = "Surin",Email = "pop@gmail.com",Photo = "59340500035.jpg")
# sth1 = Profile(id_student = 59340500021,Name = "Thipawan",Surname  = "Pairam", Sex = "Miss",Dateofbirth = "14/09/40",Birthplace = "Hospital1",Nationality = "Thai",Education = "Bungkan",Relative = "Dad",PhoneforEmergency = "0941234567",Phonestudent = "0867654321" ,Address = "Bungkan",Email = "pair@gmail.com",Photo = "59340500021.jpg")
# sth2 = Profile(id_student = 59340500017,Name = "Natthaphon",Surname  = "Sudadech", Sex = "Mr", Dateofbirth = "05/03/39",Birthplace = "Hospital2",Nationality = "Thai",Education = "Bungkan",Relative = "Mom",PhoneforEmergency = "087654321",Phonestudent = "0865432111" ,Address = "Bungkan",Email = "mill@gmail.com",Photo = "59340500017.jpg")
# sth3 = Profile(id_student = 58340500011,Name = "Chanittha",Surname  = "Techasombooranakit", Sex = "Miss", Dateofbirth = "11/10/39",Birthplace = "Hospital3",Nationality = "Thai",Education = "Banakok",Relative = "Dad",PhoneforEmergency = "067894332",Phonestudent = "087625434" ,Address = "Bangkok",Email = "winnie@gmail.com",Photo = "58340500011.jpg")
# sth4 = Profile(id_student = 58340500014,Name = "Chawisorn",Surname  = "Samrit", Sex = "Mr", Dateofbirth = "21/01/39",Birthplace = "Hospital4",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "09999999999",Phonestudent = "08799999" ,Address = "Bangkok",Email = "green@gmail.com",Photo = "58340500014.jpg")
# sth5 = Profile(id_student = 57340500008,Name = "Chakputtana",Surname  = "Sangpradit", Sex = "Miss", Dateofbirth = "24/05/38",Birthplace = "Hospital5",Nationality = "Thai",Education = "Saraburi",Relative = "Dad",PhoneforEmergency = "0891111111",Phonestudent = "0871111111" ,Address = "Bangkok",Email = "sod@gmail.com",Photo = "57340500008.jpg")
# sth6 = Profile(id_student = 57340500016,Name = "Nuttida",Surname  = "Peeklom", Sex = "Miss", Dateofbirth = "12/06/38",Birthplace = "Hospital6",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "0812222222",Phonestudent = "078888888" ,Address = "Bangkok",Email = "tan@gmail.com",Photo = "57340500016.jpg")
# sth7 = Profile(id_student = 60340500004,Name = "Kelwalee",Surname  = "rattanasakulthong", Sex = "Miss", Dateofbirth = "19/08/41",Birthplace = "Hospital7",Nationality = "Thai",Education = "Banakok",Relative = "Dad",PhoneforEmergency = "0934444444",Phonestudent = "0954444444" ,Address = "Bangkok",Email = "kel@gmail.com",Photo = "60340500004.jpg")
# sth8 = Profile(id_student = 60340500050,Name = "Lanna",Surname  = "Foolek", Sex = "Miss", Dateofbirth = "30/05/41",Birthplace = "Hospital8",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "0941111111",Phonestudent = "061111111" ,Address = "Bangkok",Email = "mai@gmail.com",Photo = "60340500050.jpg")
sth = Profile(id_student=59340500001,Name="Kanyarat",Surname="Kovitmongkol",Sex="Miss",Dateofbirth="07/09/2540",Birthplace="Hospital01",Nationality="Thai",Education="School01",Relative="Mom01",PhoneforEmergency="0000000001",Phonestudent="0100000000",Address="Home01",Email="01@gmail.com",Photo="59340500001.jpg")
sth1 = Profile(id_student=59340500002,Name="Kittipop",Surname="liaosuthamat",Sex="Mr",Dateofbirth="27/01/2540",Birthplace="Hospital02",Nationality="Thai",Education="School02",Relative="Mom02",PhoneforEmergency="0000000002",Phonestudent="0200000000",Address="Home02",Email="02@gmail.com",Photo="59340500002.jpg")
sth2 = Profile(id_student=59340500004,Name="Kelwalee",Surname="Rattanasakulthong",Sex="Miss",Dateofbirth="18/12/2540",Birthplace="Hospital04",Nationality="Thai",Education="School04",Relative="Mom04",PhoneforEmergency="0000000004",Phonestudent="0400000000",Address="Home04",Email="04@gmail.com",Photo="59340500004.jpg")
sth3 = Profile(id_student=59340500005,Name="Kanut",Surname="Thummaruksa",Sex="Mr",Dateofbirth="00/00/0000",Birthplace="Hospital05",Nationality="Thai",Education="School05",Relative="Mom05",PhoneforEmergency="0000000005",Phonestudent="0500000000",Address="Home05",Email="05@gmail.com",Photo="59340500005.jpg")
sth4 = Profile(id_student=59340500006,Name="Komkrit",Surname="Thonbunchu",Sex="Mr",Dateofbirth="11/12/2540",Birthplace="Hospital06",Nationality="Thai",Education="School06",Relative="Mom06",PhoneforEmergency="0000000006",Phonestudent="0600000000",Address="Home06",Email="06@gmail.com",Photo="59340500006.jpg")
sth5 = Profile(id_student=59340500008,Name="Chakputtana",Surname="Sangpradit",Sex="Mr",Dateofbirth="20/02/2541",Birthplace="Hospital08",Nationality="Thai",Education="School08",Relative="Mom08",PhoneforEmergency="0000000008",Phonestudent="0800000000",Address="Home08",Email="08@gmail.com",Photo="59340500008.jpg")
sth6 = Profile(id_student=59340500009,Name="Chonapat",Surname="Kitprasert",Sex="Mr",Dateofbirth="00/00/0000",Birthplace="Hospital09",Nationality="Thai",Education="School09",Relative="Mom09",PhoneforEmergency="0000000009",Phonestudent="0900000000",Address="Home09",Email="09@gmail.com",Photo="59340500009.jpg")
sth7 = Profile(id_student=59340500010,Name="Chanagan",Surname="Kanokwattananon",Sex="Miss",Dateofbirth="25/07/2540",Birthplace="Hospital10",Nationality="Thai",Education="School10",Relative="Mom10",PhoneforEmergency="0000000010",Phonestudent="1000000000",Address="Home10",Email="10@gmail.com",Photo="59340500010.jpg")
sth8 = Profile(id_student=59340500011,Name="Chanittha",Surname="Techasombooranakit",Sex="Miss",Dateofbirth="26/06/2541",Birthplace="Hospital11",Nationality="Thai",Education="School11",Relative="Mom11",PhoneforEmergency="0000000011",Phonestudent="1100000000",Address="Home11",Email="11@gmail.com",Photo="59340500011.jpg")
sth9 = Profile(id_student=59340500012,Name="Chalita",Surname="Rattanopas",Sex="Miss",Dateofbirth="24/04/2540",Birthplace="Hospital12",Nationality="Thai",Education="School12",Relative="Mom12",PhoneforEmergency="0000000012",Phonestudent="1200000000",Address="Home12",Email="12@gmail.com",Photo="59340500012.jpg")
sth10 = Profile(id_student=59340500013,Name="Chawakorn",Surname="Chaichanawirote",Sex="Mr",Dateofbirth="09/06/2540",Birthplace="Hospital13",Nationality="Thai",Education="School13",Relative="Mom13",PhoneforEmergency="0000000013",Phonestudent="1300000000",Address="Home13",Email="13@gmail.com",Photo="59340500013.jpg")
sth11 = Profile(id_student=59340500014,Name="Chawisorn",Surname="Samrit",Sex="Mr",Dateofbirth="20/11/2540",Birthplace="Hospital14",Nationality="Thai",Education="School14",Relative="Mom14",PhoneforEmergency="0000000014",Phonestudent="1400000000",Address="Home14",Email="14@gmail.com",Photo="59340500014.jpg")
sth12 = Profile(id_student=59340500015,Name="Natanon",Surname="Trangratanajit",Sex="Mr",Dateofbirth="20/06/2540",Birthplace="Hospital15",Nationality="Thai",Education="School15",Relative="Mom15",PhoneforEmergency="0000000015",Phonestudent="1500000000",Address="Home15",Email="15@gmail.com",Photo="59340500015.jpg")
sth13 = Profile(id_student=59340500016,Name="Nuttida",Surname="Peeklom",Sex="Miss",Dateofbirth="22/03/2541",Birthplace="Hospital16",Nationality="Thai",Education="School16",Relative="Mom16",PhoneforEmergency="0000000016",Phonestudent="1600000000",Address="Home16",Email="16@gmail.com",Photo="59340500016.jpg")
sth14 = Profile(id_student=59340500017,Name="Natthaphon",Surname="Sudadech",Sex="Mr",Dateofbirth="27/08/2540",Birthplace="Hospital17",Nationality="Thai",Education="School17",Relative="Mom17",PhoneforEmergency="0000000017",Phonestudent="1700000000",Address="Home17",Email="17@gmail.com",Photo="59340500017.jpg")
sth15 = Profile(id_student=59340500018,Name="Natworpong",Surname="Loyswai",Sex="Mr",Dateofbirth="06/04/2541",Birthplace="Hospital18",Nationality="Thai",Education="School18",Relative="Mom18",PhoneforEmergency="0000000018",Phonestudent="1800000000",Address="Home18",Email="18@gmail.com",Photo="59340500018.jpg")
sth16 = Profile(id_student=59340500019,Name="Nuttawat",Surname="Chantraphakorn",Sex="Mr",Dateofbirth="19/01/2541",Birthplace="Hospital19",Nationality="Thai",Education="School19",Relative="Mom19",PhoneforEmergency="0000000019",Phonestudent="1900000000",Address="Home19",Email="19@gmail.com",Photo="59340500019.jpg")
sth17 = Profile(id_student=59340500020,Name="Tretap",Surname="Promwiset",Sex="Mr",Dateofbirth="16/05/2541",Birthplace="Hospital20",Nationality="Thai",Education="School20",Relative="Mom20",PhoneforEmergency="0000000020",Phonestudent="2000000000",Address="Home20",Email="20@gmail.com",Photo="59340500020.jpg")
sth18 = Profile(id_student=59340500021,Name="Thipawan",Surname="Pairam",Sex="Miss",Dateofbirth="14/02/2540",Birthplace="Hospital21",Nationality="Thai",Education="School21",Relative="Mom21",PhoneforEmergency="0000000021",Phonestudent="2100000000",Address="Home21",Email="21@gmail.com",Photo="59340500021.jpg")
sth19 = Profile(id_student=59340500022,Name="Thanatorn",Surname="Khumrang",Sex="Mr",Dateofbirth="27/07/2541",Birthplace="Hospital22",Nationality="Thai",Education="School22",Relative="Mom22",PhoneforEmergency="0000000022",Phonestudent="2200000000",Address="Home22",Email="22@gmail.com",Photo="59340500022.jpg")
sth20 = Profile(id_student=59340500023,Name="Dhamdhawach",Surname="Horsuwan",Sex="Mr",Dateofbirth="07/10/2540",Birthplace="Hospital23",Nationality="Thai",Education="School23",Relative="Mom23",PhoneforEmergency="0000000023",Phonestudent="2300000000",Address="Home23",Email="23@gmail.com",Photo="59340500023.jpg")
sth21 = Profile(id_student=59340500024,Name="Tassamon",Surname="Jarubenjaluck",Sex="Miss",Dateofbirth="06/07/2541",Birthplace="Hospital24",Nationality="Thai",Education="School24",Relative="Mom24",PhoneforEmergency="0000000024",Phonestudent="2400000000",Address="Home24",Email="24@gmail.com",Photo="59340500024.jpg")
sth22 = Profile(id_student=59340500025,Name="Tachadol",Surname="Suthisomboon",Sex="Mr",Dateofbirth="12/09/2540",Birthplace="Hospital25",Nationality="Thai",Education="School25",Relative="Mom25",PhoneforEmergency="0000000025",Phonestudent="2500000000",Address="Home25",Email="25@gmail.com",Photo="59340500025.jpg")
sth23 = Profile(id_student=59340500026,Name="Thunchanok",Surname="Phutthaphaiboon",Sex="Miss",Dateofbirth="15/12/2540",Birthplace="Hospital26",Nationality="Thai",Education="School26",Relative="Mom26",PhoneforEmergency="0000000026",Phonestudent="2600000000",Address="Home26",Email="26@gmail.com",Photo="59340500026.jpg")
sth24 = Profile(id_student=59340500027,Name="Teeravorn",Surname="Apichanapong",Sex="Mr",Dateofbirth="20/11/2540",Birthplace="Hospital27",Nationality="Thai",Education="School27",Relative="Mom27",PhoneforEmergency="0000000027",Phonestudent="2700000000",Address="Home27",Email="27@gmail.com",Photo="59340500027.jpg")
sth25 = Profile(id_student=59340500028,Name="Nontapat",Surname="Sumalnop",Sex="Mr",Dateofbirth="27/10/2540",Birthplace="Hospital28",Nationality="Thai",Education="School28",Relative="Mom28",PhoneforEmergency="0000000028",Phonestudent="2800000000",Address="Home28",Email="28@gmail.com",Photo="59340500028.jpg")
sth26 = Profile(id_student=59340500029,Name="Noppasorn",Surname="Larpkiattaworn",Sex="Miss",Dateofbirth="27/04/2541",Birthplace="Hospital29",Nationality="Thai",Education="School29",Relative="Mom29",PhoneforEmergency="0000000029",Phonestudent="2900000000",Address="Home29",Email="29@gmail.com",Photo="59340500029.jpg")
sth27 = Profile(id_student=59340500030,Name="Nantaluk",Surname="Ployraya",Sex="Miss",Dateofbirth="05/01/2541",Birthplace="Hospital30",Nationality="Thai",Education="School30",Relative="Mom30",PhoneforEmergency="0000000030",Phonestudent="3000000000",Address="Home30",Email="30@gmail.com",Photo="59340500030.jpg")
sth28 = Profile(id_student=59340500032,Name="Pathompong",Surname="Sinngam",Sex="Mr",Dateofbirth="18/02/2541",Birthplace="Hospital32",Nationality="Thai",Education="School32",Relative="Mom32",PhoneforEmergency="0000000032",Phonestudent="3200000000",Address="Home32",Email="32@gmail.com",Photo="59340500032.jpg")
sth29 = Profile(id_student=59340500033,Name="Parpada",Surname="Piamjinda",Sex="Miss",Dateofbirth="02/05/2540",Birthplace="Hospital33",Nationality="Thai",Education="School33",Relative="Mom33",PhoneforEmergency="0000000033",Phonestudent="3300000000",Address="Home33",Email="33@gmail.com",Photo="59340500033.jpg")
sth30 = Profile(id_student=59340500034,Name="Poramet",Surname="Pond",Sex="Mr",Dateofbirth="00/00/0000",Birthplace="Hospital34",Nationality="Thai",Education="School34",Relative="Mom34",PhoneforEmergency="0000000034",Phonestudent="3400000000",Address="Home34",Email="34@gmail.com",Photo="59340500034.jpg")
sth31 = Profile(id_student=59340500035,Name="Panchalee",Surname="Sookprao",Sex="Miss",Dateofbirth="29/05/2540",Birthplace="Hospital35",Nationality="Thai",Education="School35",Relative="Mom35",PhoneforEmergency="0000000035",Phonestudent="3500000000",Address="Home35",Email="35@gmail.com",Photo="59340500035.jpg")
sth32 = Profile(id_student=59340500036,Name="Pitijit",Surname="Chareonwuttikajorn",Sex="Miss",Dateofbirth="21/01/2541",Birthplace="Hospital36",Nationality="Thai",Education="School36",Relative="Mom36",PhoneforEmergency="0000000036",Phonestudent="3600000000",Address="Home36",Email="36@gmail.com",Photo="59340500036.jpg")
sth33 = Profile(id_student=59340500037,Name="Pimanee",Surname="Seesorn",Sex="Mr",Dateofbirth="04/03/2540",Birthplace="Hospital37",Nationality="Thai",Education="School37",Relative="Mom37",PhoneforEmergency="0000000037",Phonestudent="3700000000",Address="Home37",Email="37@gmail.com",Photo="59340500037.jpg")
sth34 = Profile(id_student=59340500038,Name="Piya",Surname="Chatthaicharoen",Sex="Mr",Dateofbirth="23/10/2540",Birthplace="Hospital38",Nationality="Thai",Education="School38",Relative="Mom38",PhoneforEmergency="0000000038",Phonestudent="3800000000",Address="Home38",Email="38@gmail.com",Photo="59340500038.jpg")
sth35 = Profile(id_student=59340500039,Name="Pongsakorn",Surname="Meena",Sex="Mr",Dateofbirth="06/10/2540",Birthplace="Hospital39",Nationality="Thai",Education="School39",Relative="Mom39",PhoneforEmergency="0000000039",Phonestudent="3900000000",Address="Home39",Email="39@gmail.com",Photo="59340500039.jpg")
sth36 = Profile(id_student=59340500040,Name="Pornpawee",Surname="Srithan",Sex="Miss",Dateofbirth="11/12/2541",Birthplace="Hospital40",Nationality="Thai",Education="School40",Relative="Mom40",PhoneforEmergency="0000000040",Phonestudent="4000000000",Address="Home40",Email="40@gmail.com",Photo="59340500040.jpg")
sth37 = Profile(id_student=59340500041,Name="Phatchariya",Surname="Laousittisuk",Sex="Miss",Dateofbirth="28/02/2541",Birthplace="Hospital41",Nationality="Thai",Education="School41",Relative="Mom41",PhoneforEmergency="0000000041",Phonestudent="4100000000",Address="Home41",Email="41@gmail.com",Photo="59340500041.jpg")
sth38 = Profile(id_student=59340500043,Name="Phakaphol",Surname="Sangkaew",Sex="Mr",Dateofbirth="22/07/2540",Birthplace="Hospital43",Nationality="Thai",Education="School43",Relative="Mom43",PhoneforEmergency="0000000043",Phonestudent="4300000000",Address="Home43",Email="43@gmail.com",Photo="59340500043.jpg")
sth39 = Profile(id_student=59340500044,Name="Pattaraporn",Surname="Punya",Sex="Miss",Dateofbirth="12/01/2540",Birthplace="Hospital44",Nationality="Thai",Education="School44",Relative="Mom44",PhoneforEmergency="0000000044",Phonestudent="4400000000",Address="Home44",Email="44@gmail.com",Photo="59340500044.jpg")
sth40 = Profile(id_student=59340500045,Name="Phubodee",Surname="Tantipalaphol",Sex="Mr",Dateofbirth="24/09/2540",Birthplace="Hospital45",Nationality="Thai",Education="School45",Relative="Mom45",PhoneforEmergency="0000000045",Phonestudent="4500000000",Address="Home45",Email="45@gmail.com",Photo="59340500045.jpg")
sth41 = Profile(id_student=59340500047,Name="Phusana",Surname="Phatnut",Sex="Mr",Dateofbirth="28/11/2540",Birthplace="Hospital47",Nationality="Thai",Education="School47",Relative="Mom47",PhoneforEmergency="0000000047",Phonestudent="4700000000",Address="Home47",Email="47@gmail.com",Photo="59340500047.jpg")
sth42 = Profile(id_student=59340500048,Name="Yotsaphat",Surname="lertsukon",Sex="Mr",Dateofbirth="23/08/2540",Birthplace="Hospital48",Nationality="Thai",Education="School48",Relative="Mom48",PhoneforEmergency="0000000048",Phonestudent="4800000000",Address="Home48",Email="48@gmail.com",Photo="59340500048.jpg")
sth43 = Profile(id_student=59340500049,Name="Ratthanin",Surname="Kittisriphong",Sex="Mr",Dateofbirth="08/08/2540",Birthplace="Hospital49",Nationality="Thai",Education="School49",Relative="Mom49",PhoneforEmergency="0000000049",Phonestudent="4900000000",Address="Home49",Email="49@gmail.com",Photo="59340500049.jpg")
sth44 = Profile(id_student=59340500050,Name="Lanna",Surname="Foolek",Sex="Miss",Dateofbirth="20/06/2540",Birthplace="Hospital50",Nationality="Thai",Education="School50",Relative="Mom50",PhoneforEmergency="0000000050",Phonestudent="5000000000",Address="Home50",Email="50@gmail.com",Photo="59340500050.jpg")

sth45 = Profile(id_student = 58340500011,Name = "Chanittha",Surname  = "Techasombooranakit", Sex = "Miss", Dateofbirth = "11/10/39",Birthplace = "Hospital3",Nationality = "Thai",Education = "Banakok",Relative = "Dad",PhoneforEmergency = "067894332",Phonestudent = "087625434" ,Address = "Bangkok",Email = "winnie@gmail.com",Photo = "58340500011.jpg")
sth46 = Profile(id_student = 58340500014,Name = "Chawisorn",Surname  = "Samrit", Sex = "Mr", Dateofbirth = "21/01/39",Birthplace = "Hospital4",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "09999999999",Phonestudent = "08799999" ,Address = "Bangkok",Email = "green@gmail.com",Photo = "58340500014.jpg")
sth47 = Profile(id_student = 57340500008,Name = "Chakputtana",Surname  = "Sangpradit", Sex = "Miss", Dateofbirth = "24/05/38",Birthplace = "Hospital5",Nationality = "Thai",Education = "Saraburi",Relative = "Dad",PhoneforEmergency = "0891111111",Phonestudent = "0871111111" ,Address = "Bangkok",Email = "sod@gmail.com",Photo = "57340500008.jpg")
sth48 = Profile(id_student = 57340500016,Name = "Nuttida",Surname  = "Peeklom", Sex = "Miss", Dateofbirth = "12/06/38",Birthplace = "Hospital6",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "0812222222",Phonestudent = "078888888" ,Address = "Bangkok",Email = "tan@gmail.com",Photo = "57340500016.jpg")
sth49 = Profile(id_student = 60340500004,Name = "Kelwalee",Surname  = "rattanasakulthong", Sex = "Miss", Dateofbirth = "19/08/41",Birthplace = "Hospital7",Nationality = "Thai",Education = "Banakok",Relative = "Dad",PhoneforEmergency = "0934444444",Phonestudent = "0954444444" ,Address = "Bangkok",Email = "kel@gmail.com",Photo = "60340500004.jpg")
sth50 = Profile(id_student = 60340500050,Name = "Lanna",Surname  = "Foolek", Sex = "Miss", Dateofbirth = "30/05/41",Birthplace = "Hospital8",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "0941111111",Phonestudent = "061111111" ,Address = "Bangkok",Email = "mai@gmail.com",Photo = "60340500050.jpg")

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
session.add(sth10) #add sth into database.
session.add(sth11) #add sth into database.
session.add(sth12) #add sth into database.
session.add(sth13) #add sth into database.
session.add(sth14) #add sth into database.
session.add(sth15) #add sth into database.
session.add(sth16) #add sth into database.
session.add(sth17) #add sth into database.
session.add(sth18) #add sth into database.
session.add(sth19) #add sth into database.
session.add(sth20) #add sth into database.
session.add(sth21) #add sth into database.
session.add(sth22) #add sth into database.
session.add(sth23) #add sth into database.
session.add(sth24) #add sth into database.
session.add(sth25) #add sth into database.
session.add(sth26) #add sth into database.
session.add(sth27) #add sth into database.
session.add(sth28) #add sth into database.
session.add(sth29) #add sth into database.
session.add(sth30) #add sth into database.
session.add(sth31) #add sth into database.
session.add(sth31) #add sth into database.
session.add(sth32) #add sth into database.
session.add(sth33) #add sth into database.
session.add(sth34) #add sth into database.
session.add(sth35) #add sth into database.
session.add(sth36) #add sth into database.
session.add(sth37) #add sth into database.
session.add(sth38) #add sth into database.
session.add(sth39) #add sth into database.
session.add(sth40) #add sth into database.
session.add(sth41) #add sth into database.
session.add(sth42) #add sth into database.
session.add(sth43) #add sth into database.
session.add(sth44) #add sth into database.
session.add(sth45) #add sth into database.
session.add(sth46) #add sth into database.
session.add(sth47) #add sth into database.
session.add(sth48) #add sth into database.
session.add(sth49) #add sth into database.
session.add(sth50) #add sth into database.


sth = Activity(id = 1,id_student = 59340500017,NameActivity = "Natthaphon",Description = "this is so fun.",Photo = "Natthaphon.jpg",Type = "Dynamics",Advisor = "AJ.Ton",Date_Activity = "14/12/60",File = "Natthaphon.docx",Confirm = "Not Confirm yet")
sth1 = Activity(id = 1,id_student = 59340500021,NameActivity = "Thipawan",Description = "Receive a lot of knowledges.",Photo = "Thipawan.jpg",Type = "Calculas",Advisor = "AJ.Somran",Date_Activity = "15/12/61",File = "Thipawan.pdf",Confirm = "Confirm")
sth2 = Activity(id = 1,id_student = 59340500035,NameActivity = "Panchalee",Description = "It is will be useful.",Photo = "Panchalee.jpg",Type = "Digital",Advisor = "AJ.Pi",Date_Activity = "15/12/60",File = "Panchalee.txt",Confirm = "Confirm")
sth3 = Activity(id = 1,id_student = 59340500035,NameActivity = "Tabletennnis",Description = "Table tennis is good.",Photo = "Tabletennnis.jpg",Type = "Sport",Advisor = "AJ.__",Date_Activity = "29/05/60",File = "Tabletennnis.docx",Confirm = "Confirm")
sth4 = Activity(id = 1,id_student = 58340500011,NameActivity = "Project",Description = "This project is very hard.",Photo = "Project.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "19/10/61",File = "Project.pdf",Confirm = "Not Confirm yet")
sth5 = Activity(id = 1,id_student = 57340500008,NameActivity = "FootballKMUTT",Description = "This is my favorite sport.",Photo = "FootballKMUTT.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "20/10/61",File = "FootballKMUTT.pdf",Confirm = "Confirm ")
sth6 = Activity(id = 1,id_student = 57340500016,NameActivity = "Chorus",Description = "This is my favorite hobbit.",Photo = "Chorus.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "21/10/61",File = "Chorus.docx",Confirm = "Not Confirm yet")
sth7 = Activity(id = 1,id_student = 58340500014,NameActivity = "SuperRobot",Description = "This is my favorite hobbit.",Photo = "SuperRobot.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "22/10/61",File = "SuperRobot.pptx",Confirm = "Not Confirm yet")
sth8 = Activity(id = 1,id_student = 60340500004,NameActivity = "CatRobot",Description = "This is my favorite animal.",Photo = "CatRobot.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "23/10/61",File = "CatRobot.xlsx",Confirm = "Confirm")
sth9 = Activity(id = 1,id_student = 60340500050,NameActivity = "DesignUI",Description = "This is my favorite work.",Photo = "DesignUI.jpg",Type = "Research",Advisor = "AJ.__",Date_Activity = "24/10/61",File = "DesignUI.txt",Confirm = "Not Confirm yet")

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
sth7 = StudentPW(id_student = 60340500004,S_Password = "60340500004")
sth8 = StudentPW(id_student = 60340500050,S_Password = "60340500050")
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
