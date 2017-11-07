from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from Profile import Profile
import sqlite3
import sys

app = Flask(__name__)

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
	return(getID)

@app.route('/getPass', methods=['POST'])
def getPass():
	getPassword = getIDPass().get('pass', None)
	return(getPassword)

@app.route('/checkPerson', methods=['POST'])
def checkPerson():
	getID = getIDPass().get('id', None)
	getPassword = getIDPass().get('pass', None)

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
		return render_template('homeStudent.html', id_user = getID)
	elif countID == 2 and countPass == 0:
		print('your password is incorrect')
	else:
		return render_template('homeTeacherofficer.html')
	conn.close()

@app.route('/menubar', methods=['POST'])
def menubar():
	getMenubar = request.form['click']
	print(getMenubar)
	if getMenubar == 'PROFILE':
		return render_template('profile.html')
	if getMenubar == 'ACADEMIC':
		return render_template('AcademicStudent.html')
	if getMenubar == 'WORK&EXPERIENCE':
		return render_template('activity.html')

@app.route('/printer', methods=['POST'])
def test():
	printer = request.form['click']
	print(printer)

'''@app.route('/test', methods=['POST'])
def test():
	getTest = request.form['click']
	print(getTest)'''

app.run(debug=True)
