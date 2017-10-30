from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

test = Flask(__name__)


@test.route('/')
def html():
	return render_template('edit-activity.html')

@test.route('/getPopup', methods=['POST'])
def getPopup():

    getPopup = request.form['yes']

    print(getPopup)
test.run(debug=True)
