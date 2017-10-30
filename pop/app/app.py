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

app = Flask(__name__)

keepID = keepID()
keepHistory = keepHistory()
pullData = pullData()

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
	re = return_Method(getID)
	name = re.name()
	keepID.Name = name
	print(keepID.Name)

	conn = sqlite3.connect('IDPassStudent.db')
	countID = 0
	countPass = 0
	atRow = 0
	with conn:
		cur = conn.cursor()
		cur.execute("SELECT * FROM IDPASS")
		rows = cur.fetchall()
		countRow = 0
		for row in rows:
			countRow += 1
			for i in range(countRow):
				for row in rows[i]:
					if str(row) == getID:
						countID += 1
						atRow = i
						break;
					else:
						countID += 0
		for row in rows[atRow]:
				if str(row) == getPassword:
					countPass += 1
					break;
				else:
					countPass += 0
	#print(countID)
	#print(countPass)
	if countID > 1 and countPass == 1:
		name = keepID.Name
		print(keepID.Name)
		keepHistory.keep_page('homeStudent.html', None)
		return render_template('homeStudent.html', id_user=getID, name=name)
	elif countID == 2 and countPass == 0:
		print('your password is incorrect')
	else:
		return render_template('homeTeacherofficer.html')
	conn.close()

@app.route('/menubar', methods=['POST'])
def menubar():
	getMenubar = request.form['click']
	print(getMenubar)
	getID = keepID.ID
	name = keepID.Name

	if getMenubar == 'PROFILE':
		keepHistory.keep_page('profile.html', pullData.Profile(getID))
		return render_template('profile.html', name=name, page=pullData.Profile(getID))
	if getMenubar == 'ACADEMIC':
		keepHistory.keep_page('AcademicStudent.html', pullData.Academic_term(getID),pullData.Academic_sum(getID))
		return render_template('AcademicStudent.html', name=name, page=pullData.Academic_term(getID), page2=pullData.Academic_sum(getID))
	if getMenubar == 'WORK&EXPERIENCE':
		keepHistory.keep_page('activity.html', pullData.Activity(getID))
		return render_template('activity.html', name=name, page=pullData.Activity(getID))
	if getMenubar == 'home_icon':
		keepHistory.keep_page('homeStudent.html', None)
		return render_template('homeStudent.html', name=name, id_user=getID)
	if getMenubar == 'print_icon':
		keepHistory.keep_page('print_choose.html', None)
		print(getMenubar)
		return render_template('print_choose.html')
	if getMenubar == 'logout_icon':
		print(getMenubar)
		keepHistory.reset_keepHistory()
		keepID.reset_keepID()
		return render_template('login.html')
	if getMenubar == 'back':
		print(getMenubar)
		keepHistory.print_listPage()
		history = keepHistory.history()
		Value = keepHistory.Value_page()
		Value2 = keepHistory.Value2_page()
		return render_template(history,id_user=getID, name=name, page = Value, page2 = Value2)

@app.route('/printer', methods=['POST'])
def printer():
	printer = request.form['click']
	getID = keepID.ID
	name = keepID.Name
	#keepID.Print_ID()

	keepHistory.keep_page('print_choose.html', None)
	print(printer)
	return render_template('print_choose.html', name=name)

@app.route('/selectTerm', methods=['POST'])
def selectTerm():
	getSelectTerm = request.form['click']
	print(getSelectTerm)
	getID = keepID.ID
	name = keepID.Name
	if getSelectTerm == '1/2559':
		term = '1/2559'
	if getSelectTerm == '2/2559':
		term = '2/2559'
	if getSelectTerm == '1/2560':
		term = '1/2560'
	if getSelectTerm == '2/2560':
		term = '2/2560'
	return render_template('AcademicStudent.html', name=name, page=pullData.Academic_term(getID,term),page2=pullData.Academic_sum(getID,term))

@app.route('/moreinfo', methods=['POST'])
def moreinfo():
	getMoreinfo = request.form['click']
	getID = keepID.ID
	name = keepID.Name

	if getMoreinfo == 'MORE INFO>>':
		keepHistory.keep_page('dataactivity.html', pullData.Activity(getID))
		keepHistory.print_listPage()
		return render_template('dataactivity.html', name=name, page=pullData.Activity(getID))

@app.route('/editInfo', methods=['POST'])
def editInfo():
	getEditInfo = request.form['click']
	getID = keepID.ID
	name = keepID.Name
	if getEditInfo == 'EDIT':
		return render_template('edit-your-infomation.html', name=name)

@app.route('/editAc', methods=['POST'])
def editAc():
	getEditAc = request.form['click']
	getID = keepID.ID
	name = keepID.Name

	if getEditAc == 'EDIT':
		keepHistory.keep_page('edit-activity.html',None)
		return render_template('edit-activity.html', name=name)

@app.route('/getEditInfo', methods=['POST'])
def getEditInfo():
	getEditInfo = dict(request.form.items())
	print(getEditInfo)
	getID = keepID.ID
	#keepID.Print_ID()
	name = keepID.Name

	return render_template('profile.html', name=name, page=pullData.Profile(getID))

@app.route('/getEditAc', methods=['POST'])
def getEditAc():
	getEditAc = dict(request.form.items())
	print(getEditAc)
	return render_template('dataactivity.html', name=name, page=pullData.Activity(getID))

@app.route('/checkBox', methods=['POST'])
def getCheckBox():
	getCheck = dict(request.form.items())
	print(getCheck)
	getCheckBox = request.form['click']
	print(getCheckBox)

	getID = keepID.ID
	name = keepID.Name

	if getCheck.get('NAME') == 'on':
		print('select name')
	if getCheck.get('date of birth') == 'on':
		print('select date of birth')
	if getCheck.get('gpax') == 'on':
		print('select gpax')
	if getCheck.get('contact') == 'on':
		print('select contact')
	if getCheck.get('congenital disease') == 'on':
		print('select congenital disease')
	if getCheck.get('nationality') == 'on':
		print('select nationality')
	if getCheck.get('birthplace') == 'on':
		print('select birthplace')
	if getCheck.get('data contact') == 'on':
		print('select data contact')

	'''name_file = str(name) + '\'s file' + '.txt'
	create = open(str(name_file),'w')'''

	if getCheckBox == 'DONE':
		return render_template(keepHistory.history(),id_user=getID, name=name, page=keepHistory.Value_page() )

@app.route('/selectall', methods=['POST'])
def selectall():
	getSelectall = request.form['click']
	getID = keepID.ID
	name = keepID.Name

	if getSelectall == 'SELECTALL':
		return render_template('print_choose_selectall.html', name=name)
	if getSelectall == 'UNSELECTALL':
		return render_template('print_choose.html', name=name)

@app.route('/getAddAc', methods=['POST'])
def getAddAc():
	getAddAc = request.form['click']
	print(getAddAc)
	getID = keepID.ID
	name = keepID.Name
	keepHistory.keep_page('edit-activity.html',None)
	return render_template('edit-activity.html', name=name)


app.run(debug=True)
