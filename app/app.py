from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import sqlite3
import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from keepID import *
from getDatabase import *
from Node_web import *
from keepHistory import *
from pullData import *
from editProfile import *
from editActivity import *
from saveText import *
import os
import os.path
import shutil
from shutil import copyfile
import shutil
from addAcademic import Input_Academics
from sortTerm import*

app = Flask(__name__)

keepID = keepID()
keepHistory = keepHistory()
pullData = pullData()
editProfile = editProfile()
editActivity = editActivity()
saveText = saveText()
sortTerm = sortTerm()

'''---------------------------------------------------------------------------------------------------------------------------------------------------'''
""" Login """

@app.route('/')
def html():
	return render_template('login.html')

@app.route('/getIDPass', methods=['POST'])
def getIDPass():
	idPass = dict(request.form.items())
	return(idPass)

@app.route('/getID', methods=['POST'])
def getID():
	getID = getIDPass().get('id', None)
	#keepID.ID = getID
	return(getID)

@app.route('/getPass', methods=['POST'])
def getPass():
	getPassword = getIDPass().get('pass', None)
	#keepID.Password = getPassword
	return(getPassword)

@app.route('/checkPerson', methods=['POST'])
def checkPerson():
	getID = getIDPass().get('id', None)
	getPassword = getIDPass().get('pass', None)
	keepID.ID = getID
	keepID.Password = getPassword
	print (getID)
	print (getPassword)
	check = Check()

	if check.S_check(getID,getPassword) :
		print (getID)
		re = return_Method(getID)
		name = re.name()
		keepID.Name = name
		print(keepID.Name)
		keepID.picS = re.photo()
		picS = keepID.picS
		keepHistory.keep_page('homeStudent.html', None )
		return render_template('homeStudent.html', id_user=getID, name=name, picS = picS)

	elif  check.T_check(getID,getPassword):
		re = return_Method(getID)
		name = re.t_name()
		keepID.Name = name
		keepHistory.keep_page('port_tea.html', None )
		return render_template('port_tea.html' , name = name )
	else :
		return render_template('login.html', error = "Username or Password is incorrect!"  )


'''end Login'''



'''---------------------------------------------------------------------------------------------------------------------------------------------------'''
""" Student """

@app.route('/menubar', methods=['POST'])
def menubar():
	getMenubar = request.form['click']
	print(getMenubar)
	getID = keepID.ID
	name = keepID.Name
	picS = keepID.picS
	check = Check()

	if getMenubar == 'PROFILE':
		keepHistory.keep_page('profile.html', pullData.Profile(getID))
		return render_template('profile.html', name=name, page=pullData.Profile(getID), picS = picS)
	if getMenubar == 'ACADEMIC':
		term = check.TERM(getID)
		print (term)
		term = sortTerm.sortTerm(term)
		AllGrade = []
		GPAX = []
		for allTerm in term :
			setG = {"Gragd":[],"GPA":[],"Term":""}
			setG["Gragd"] = pullData.Academic_term(getID,allTerm)
			setG["GPA"] = pullData.Academic_sum(getID,allTerm)
			setG["Term"] = allTerm
			AllGrade.append(setG)
			if GPAX == []:
				GPAX = pullData.Academic_sum(getID,allTerm)
		term.append("All")
		print(AllGrade)
		print(GPAX)
		keepHistory.keep_page('AcademicStudent-3-table.html', AllGrade, GPAX)
		return render_template('AcademicStudent-3-table.html', name=name,term = term,page= AllGrade, page2 = GPAX)
	if getMenubar == 'WORK&EXPERIENCE':
		keepHistory.keep_page('activity.html', pullData.Activity(getID))
		print(pullData.Activity(getID))
		return render_template('activity.html', name=name, page=pullData.Activity(getID))
	if getMenubar == 'home_icon':
		keepHistory.keep_page('homeStudent.html', None)
		return render_template('homeStudent.html', name=name, id_user=getID, picS = picS)
	if getMenubar == 'print_icon':
		keepHistory.keep_page('print_choose.html', pullData.Activity(getID))
		print(getMenubar)
		return render_template('print_choose.html', name=name, page=pullData.Activity(getID))
	if getMenubar == 'logout_icon':
		print(getMenubar)
		keepHistory.reset_keepHistory()
		keepID.reset_keepID()
		return render_template('login.html')
	if getMenubar == 'back':
		print(getMenubar)
		term = check.TERM(getID)
		term = sortTerm.sortTerm(term)
		term.append("All")
		keepHistory.print_listPage()
		history = keepHistory.history()
		Value = keepHistory.Value_page()
		Value2 = keepHistory.Value2_page()
		if history == 'activity.html':
			Value = pullData.Activity(getID)
		return render_template(history,id_user=getID, name=name, page = Value, page2 = Value2, picS = picS, term = term)

@app.route('/printer', methods=['POST'])
def printer():
	printer = request.form['click']
	getID = keepID.ID
	name = keepID.Name
	#keepID.Print_ID()

	keepHistory.keep_page('print_choose.html', pullData.Activity(getID))
	print(printer)
	return render_template('print_choose.html', name=name, page=pullData.Activity(getID))

@app.route('/selectTerm', methods=['POST'])
def selectTerm():
	getSelectTerm = request.form['click']
	print(getSelectTerm)
	getID = keepID.ID
	name = keepID.Name
	check = Check()
	term = check.TERM(getID)

	term = sortTerm.sortTerm(term)

	if getSelectTerm == "All":
		AllGrade = []
		GPAX = []
		for allTerm in term :
			setG = {"Gragd":[],"GPA":[],"Term":""}
			setG["Gragd"] = pullData.Academic_term(getID,allTerm)
			setG["GPA"] = pullData.Academic_sum(getID,allTerm)
			setG["Term"] = allTerm
			AllGrade.append(setG)
			if GPAX == []:
				GPAX = pullData.Academic_sum(getID,allTerm)
		term.append("All")
		print(AllGrade)
		print(GPAX)
		return render_template('AcademicStudent-3-table.html', name=name,term = term,page= AllGrade, page2 = GPAX)


	term.append("All")
	return render_template('AcademicStudent.html', name=name, term=term, page=pullData.Academic_term(getID,getSelectTerm),page2=pullData.Academic_sum(getID,getSelectTerm), thisTerm = getSelectTerm)

@app.route('/moreinfo', methods=['POST'])
def moreinfo():
	getMoreinfo = dict(request.form.items())
	getID = keepID.ID
	name = keepID.Name
	print(getMoreinfo)

	for A in getMoreinfo:
		Moreinfo = A.split(",")
		nameActivity = Moreinfo[0]
		idAct = Moreinfo[1]
		print(nameActivity)
		print(idAct)
		for Act in pullData.Activity(getID):
			if Act["Name_Activity"] == nameActivity :
				print(Act["Name_Activity"])
				if str(Act["id"]) == idAct:
					print(Act["id"])

					keepHistory.keep_page('dataactivity.html',Act,"")
					print (Act)
					return render_template('dataactivity.html', name=name, page= Act , page2 = "")

'''
	if getMoreinfo == 'MORE INFO>>':
		keepHistory.keep_page('dataactivity.html', pullData.Activity(getID))
		keepHistory.print_listPage()
		return render_template('dataactivity.html', name=name, page=pullData.Activity(getID))
'''

@app.route('/editInfo', methods=['POST'])
def editInfo():
	getEditInfo = request.form['click']
	getID = keepID.ID
	name = keepID.Name
	if getEditInfo == 'EDIT':
		keepHistory.keep_page('profile.html', pullData.Profile(getID))  #hereeeeeeeeeeeeeeeeeeeee
		return render_template('edit-your-infomation.html', name=name)

@app.route('/editAcButton', methods=['POST'])
def editAcButton():
	getEditAc = dict(request.form.items())
	print(getEditAc)
	getID = keepID.ID
	name = keepID.Name

	for A in getEditAc :
		act = A.split(",")
		nameActivity = act[0]
		idAct = act[1]
		print(nameActivity)
		print(idAct)

		for Act in pullData.Activity(getID):
			if Act["Name_Activity"] == nameActivity :
				if str(Act["id"]) == idAct:
					keepHistory.keep_page('dataactivity.html',Act)
					return render_template('edit-activity.html', name=name, page= Act["Name_Activity"], page2 = Act["id"])

'''
	if getEditAc == 'EDIT':
		keepHistory.keep_page('edit-activity.html',None)
		return render_template('edit-activity.html', name=name) '''

@app.route('/getEditInfo', methods=['POST'])
def getEditInfo():
	getEditInfo = dict(request.form.items())
	print(getEditInfo)
	getID = keepID.ID
	#keepID.Print_ID()
	picS = keepID.picS

	editProfile.edit(getID,getEditInfo)

	re = return_Method(getID)
	name = re.name()
	keepID.Name = name

	history = keepHistory.history()

	return render_template(history , name=name, page=pullData.Profile(getID), picS = picS)

@app.route('/getEditAc', methods=['POST'])
def getEditAc():
	getEditAc = dict(request.form.items())
	getID = keepID.ID
	name = keepID.Name

	print(getEditAc)
	for i in getEditAc:
		if getEditAc[i] == "SAVE":
			act = i.split(",")
			nameActivity = act[0]
			idAct = act[1]
			print(nameActivity)
			print(idAct)

	# for nameAct in getEditAc:
	# 	if nameAct != 'type' and nameAct != 'advisor'and nameAct != 'des' and nameAct != 'date':
	# 		print(nameAct)
	# 		Name_act = nameAct

	editActivity.edit(getID,nameActivity,getEditAc,idAct)

	for Act in pullData.Activity(getID):
		if Act["Name_Activity"] == nameActivity :
			if str(Act["id"]) == idAct :
				history = keepHistory.history()
				return render_template(history , name=name, page= Act)

@app.route('/checkBox', methods=['POST'])
def getCheckBox():
	getCheck = dict(request.form.items())
	print(getCheck)
	getCheckBox = request.form['click']
	print(getCheckBox)

	getID = keepID.ID
	name = keepID.Name

	re = return_Method(getID)
	s = Get_Academic(getID,None)

	ProfileAndAcademic = []
	data = {'name':re.name(),'sur':re.surname(),'dateofbirth':re.date(),'nation':re.nation(),'gpax':'-','contact':'','phone':'','address':'','email':'','dis':'','birthplace':''}
	Activity = []

	if getCheck.get('gpax') == 'on':
		data['gpax'] = ''.join(s.get_GPAX())
		print('select gpax')
	if getCheck.get('contact') == 'on':
		data['contact'] = "CONTACT"
		data['phone'] = "PHONE : " + re.Phonestu()
		data['address'] = "ADDRESS : " +  re.address()
		data['email'] = "EMAIL : " + re.email()
		print('select contact')
	if getCheck.get('congenital disease') == 'on':
		data['dis'] = "CONGENITAL DISEASE : " + ','.join(re.disease())
		print('select congenital disease')
	if getCheck.get('birthplace') == 'on':
		data['birthplace'] = "BIRTH PLACE : " + re.birth()
		print('select birthplace')

	ProfileAndAcademic.append(data)

	DataActivity = pullData.Activity(getID)
	for Act in DataActivity:
		nameAct = Act["Name_Activity"]
		if getCheck.get(nameAct) == 'on' :
			Activity.append(Act)

	if getCheckBox == 'DONE':
		print(ProfileAndAcademic)
		print(Activity)
		keepHistory.keep_page('printdata.html', ProfileAndAcademic,Activity)
		return render_template('printdata.html',id_user=getID, name=name, page=ProfileAndAcademic , page2 = Activity , picS = keepID.picS)

@app.route('/selectall', methods=['POST'])
def selectall():
	getSelectall = request.form['click']
	getID = keepID.ID
	name = keepID.Name

	if getSelectall == 'SELECTALL':
		return render_template('print_choose_selectall.html', name=name, page=pullData.Activity(getID))
	if getSelectall == 'UNSELECTALL':
		return render_template('print_choose.html', name=name, page=pullData.Activity(getID))

@app.route('/getAddAcButton', methods=['POST'])
def getAddAcButton():
	getAddAc = request.form['click']
	print(getAddAc)
	getID = keepID.ID
	name = keepID.Name
	if getAddAc == 'ADD':
		keepHistory.keep_page('activity.html', pullData.Activity(getID))
		return render_template('add-activity.html', name=name)

@app.route('/getAddAc', methods=['POST'])
def getAddAc():
	getAddAc = dict(request.form.items())
	getID = keepID.ID
	name = keepID.Name
	print(getAddAc)

	if getAddAc['photo'] != "":
		save_path = 'C:/Users/' + str(os.getlogin()) + '/Desktop'
		namephoto = getAddAc['photo']
		inputfile = str(save_path) + '/' + str(namephoto)
		print(namephoto)
		copyto = 'C:/Users/' + str(os.getlogin()) + '/Documents/GitHub/FRA241_portfolio/app/static/pictures/activity/' + str(namephoto)
		copyfile(inputfile,copyto)

	if getAddAc['File'] != "":
		save_path = 'C:/Users/' + str(os.getlogin()) + '/Desktop'
		namefile = getAddAc['File']
		inputfile = str(save_path) + '/' + str(namefile)
		print(namefile)
		copyto = 'C:/Users/' + str(os.getlogin()) + '/Documents/GitHub/FRA241_portfolio/app/static/Activity/' + str(namefile)
		copyfile(inputfile,copyto)

	editActivity.add(getID,getAddAc)

	history = keepHistory.history()

	return render_template(history, name=name, page=pullData.Activity(getID))

@app.route('/getPrindataButton', methods=['POST'])
def getPrindataButton():   												#--------- save text -----------
	button = request.form['click']
	getID = keepID.ID
	name = keepID.Name

	if button == 'SAVE':
		print('save')
		profile = keepHistory.Value_page()
		activity = keepHistory.Value2_page()
		print(profile)
		print(activity)

		saveText.create(getID,profile,activity)
		ffile = 'C:/Users/' + str(os.getlogin()) + '/Documents/GitHub/FRA241_portfolio/app/Portfolio_' + str(getID) + '.pdf'
		copyto = 'C:/Users/' + str(os.getlogin()) + '/Desktop/Portfolio_' + str(getID) + '.pdf'
		copyfile(ffile,copyto)

		os.remove(ffile)

		history = keepHistory.history()
		picS = keepID.picS
		keepHistory.keep_page('homeStudent.html', None)
		return render_template('homeStudent.html', name=name, id_user=getID, picS = picS)
	if button  == 'EDIT':
		print('edit')
		return render_template('print_choose.html', name=name, page=pullData.Activity(getID))

@app.route('/getPopup', methods=['POST'])
def getPopup():
	getpopup = request.form['popup']
	print(getpopup)
	if getpopup == 'YES':
		keepHistory.reset_keepHistory()
		keepID.reset_keepID()
		return render_template('login.html')

@app.route('/getleave', methods=['POST'])
def getleave():
	getID = keepID.ID
	name = keepID.Name
	getleave = request.form['popup']
	print(getleave)
	if getleave == 'YES':
		keepHistory.print_listPage()
		history = keepHistory.history()
		if history == 'activity.html':
			Value = pullData.Activity(getID)
			return render_template(history,id_user=getID, name=name, page = Value)
		if history == 'dataactivity.html':
			Value = keepHistory.Value_page()
			return render_template(history,id_user=getID, name=name, page = Value)
		if history == 'profile.html':
			Value = pullData.Profile(getID)
			picS = keepID.picS
			return render_template(history,id_user=getID, name=name, page = Value , picS = picS)

@app.route('/deleteAc', methods=['POST'])
def getDelete():
	getDelete = dict(request.form.items())
	print(getDelete)
	getID = keepID.ID
	name = keepID.Name
	edit = Edit(getID)
	for A in getDelete :
		act = A.split(",")
		nameActivity = act[0]
		idAct = act[1]
		print(nameActivity)
		print(idAct)
		edit.deleteAct(int(idAct),nameActivity)
	history = keepHistory.history()
	Value = pullData.Activity(getID)
	return render_template(history,id_user=getID, name=name, page = Value)

@app.route('/downloadFile', methods=['POST'])
def downloadFile():
	getFile = request.form['cilck']
	getID = keepID.ID
	name = keepID.Name
	print(getFile)

	if getFile != 'None' :
		ffile = 'C:/Users/' + str(os.getlogin()) + '/Documents/GitHub/FRA241_portfolio/app/static/Activity/' + str(getFile)
		copyto = 'C:/Users/' + str(os.getlogin()) + '/Desktop/' + str(getFile)
		copyfile(ffile,copyto)

		conf = 'Download ' + str(getFile) + ' Success'

	else:
		conf = "No File"

	keepHistory.keep_page( None , None)
	history = keepHistory.history()
	Value = keepHistory.Value_page()
	return render_template(history,id_user=getID, name=name, page = Value , page2 = conf)

@app.route('/cancleEdit', methods=['POST'])
def getCancle():
	getCancle = request.form['click']
	print(getCancle)
	getID = keepID.ID
	name = keepID.Name
	picS = keepID.picS
	keepHistory.print_listPage()
	history = keepHistory.history()
	Value = keepHistory.Value_page()
	Value2 = keepHistory.Value2_page()
	if history == 'activity.html':
		Value = pullData.Activity(getID)
	return render_template(history,id_user=getID, name=name, page = Value, page2 = Value2, picS = picS)


'''end student'''

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

""" Teacher """

@app.route('/menubarTeacher', methods=['POST'])
def getMenubarTeacher():
	getmenubar = request.form['click']
	print(getmenubar)
	getID = keepID.ID
	name = keepID.Name

	if getmenubar == 'back':
		print('back')
		history = keepHistory.history()
		Value = keepHistory.Value_page()
		Value2 = keepHistory.Value2_page()
		if history == 'teacherViewProfile.html':
			re = return_Method(Value2)
			picS = re.photo()
			return render_template(history,id_user=getID, name=name, page=Value, page2=Value2, picS = picS)
		return render_template(history,id_user=getID, name=name, page=Value, page2=Value2)

	if getmenubar == 'home':
		print('home')
		keepHistory.keep_page('port_tea.html', None)
		return render_template('port_tea.html', name=name)

@app.route('/gethome', methods=['POST'])
def gethome():
	gethome = request.form['click']
	print(gethome)
	getID = keepID.ID
	name = keepID.Name

	if gethome == 'frab':
		print('frab')
		frab_O = []
		frab_T = []
		check = Check()
		frab = check.checkfrab()
		print(frab)
		for i in frab:
			if int(i[5:])%2 == 1:
				frab_O.append(i)
			elif int(i[5:])%2 == 0:
				frab_T.append(i)
		print(frab_O)
		print(frab_T)
		keepHistory.keep_page('total_frab.html', frab_O , frab_T )
		return render_template('total_frab.html', name=name, page= frab_O ,page2 = frab_T)
	if gethome == 'grade':
		print('add grade')
		return render_template('add_grade.html', name=name)

@app.route('/getFrab', methods=['POST'])
def frab():
	frab = request.form['click']
	print(frab)
	getID = keepID.ID
	name = keepID.Name
	check = Check()
	print (frab[5:])

	A = check.FRAB(frab[5:])
	print (A)
	x = []
	dataFrab = []
	for i in A:
	    x.append(i["ID"])

	x.sort()
	for i in x:
	    for j in A :
	        if j["ID"] == i:
	            dataFrab.append(j)
	            A.remove(j)
	print(dataFrab)

	keepHistory.keep_page('nametea.html', dataFrab , frab)
	return render_template('nametea.html', name=name, page = dataFrab , page2=frab)

@app.route('/getView', methods=['POST'])
def view():
	view = dict(request.form.items())
	print(view)
	getID = keepID.ID
	name = keepID.Name


	for ID in view:
		profile = pullData.Profile(ID)
		print (profile)
		re = return_Method(ID)
		picS = re.photo()
		keepHistory.keep_page('teacherViewProfile.html', profile , ID )
		return render_template('teacherViewProfile.html', name=name, page = profile , page2 = ID, picS = picS)

@app.route('/selectView', methods=['POST'])
def seect():
	select = request.form['click']
	print(select)
	getID = keepID.ID
	name = keepID.Name

	ID = keepHistory.Value2_page()
	re = return_Method(ID)
	picS = re.photo()
	if select == 'PROFILE':
		print('profile')
		profile = pullData.Profile(ID)
		return render_template('teacherViewProfile.html', name=name, page = profile , page2 = ID, picS = picS)
	if select == 'ACADEMIC':
		print('academic')
		check = Check()
		term = check.TERM(ID)
		term = sortTerm.sortTerm(term)
		AllGrade = []
		GPAX = []
		for allTerm in term :
			setG = {"Gragd":[],"GPA":[],"Term":""}
			setG["Gragd"] = pullData.Academic_term(ID,allTerm)
			setG["GPA"] = pullData.Academic_sum(ID,allTerm)
			setG["Term"] = allTerm
			AllGrade.append(setG)
			if GPAX == []:
				GPAX = pullData.Academic_sum(ID,allTerm)
		term.append("All")
		print(AllGrade)
		print(GPAX)
		return render_template('teacherViewAcademic-3-table.html', name=name,term = term, picS = picS,page= AllGrade, page2 = GPAX)
	if select == 'WORK&EXPERIENCE':
		print('activity')
		activity = pullData.Activity(ID)
		print(activity)
		return render_template('teacherViewActivity.html', name=name, page = activity, page2 = ID, picS = picS)

@app.route('/TeacherSelectTerm', methods=['POST'])
def TeacherSelectTerm():
	getSelectTerm = request.form['click']
	print(getSelectTerm)
	getID = keepID.ID
	name = keepID.Name
	ID = keepHistory.Value2_page()
	re = return_Method(ID)
	picS = re.photo()
	check = Check()
	term = check.TERM(ID)

	term = sortTerm.sortTerm(term)

	if getSelectTerm == "All":
		AllGrade = []
		GPAX = []
		for allTerm in term :
			setG = {"Gragd":[],"GPA":[],"Term":""}
			setG["Gragd"] = pullData.Academic_term(ID,allTerm)
			setG["GPA"] = pullData.Academic_sum(ID,allTerm)
			setG["Term"] = allTerm
			AllGrade.append(setG)
			if GPAX == []:
				GPAX = pullData.Academic_sum(ID,allTerm)
		term.append("All")
		print(AllGrade)
		print(GPAX)
		return render_template('teacherViewAcademic-3-table.html', name=name,term = term, picS = picS,page= AllGrade, page2 = GPAX)

	term.append("All")
	return render_template('teacherViewAcademic.html', name=name,term = term, picS = picS,page=pullData.Academic_term(ID,getSelectTerm) , page2=pullData.Academic_sum(ID,getSelectTerm) ,SelectTerm=getSelectTerm )

@app.route('/getFileGrade', methods=['POST'])
def fileGrade():
	name = keepID.Name
	fileGrade = dict(request.form.items())
	print(fileGrade)
	click = request.form['click']
	filename = request.form['fileGrade']
	term = request.form['term']
	fileAdd = str(filename) +" added."
	print(filename)

	if click == 'ADD':

		if filename == '':
			return render_template('add_grade.html', name=name)

		else:
			save_path = 'C:/Users/' + str(os.getlogin()) + '/Desktop'
			inputfile = str(save_path) + '/' + str(filename)
			print(inputfile)
			copyto = 'C:/Users/' + str(os.getlogin()) + '/Documents/GitHub/FRA241_portfolio/app/' + str(filename)
			copyfile(inputfile,copyto)
			print(copyto)

			inputFileGrade = Input_Academics(copyto, term)
			inputFileGrade.input_Academic_and_edit_data()
			who = inputFileGrade.other_student()
			print(who)

			os.remove(copyto)

			return render_template('add_grade.html', name=name, add=fileAdd)

app.run(debug=True)
