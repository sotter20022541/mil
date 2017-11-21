from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

test = Flask(__name__)

activity = [{'nameAc':'activity1', 'advisor':'advisor1', 'date':'date1', 'type':'type1', 'des':'des1', 'file':'file1'},
            {'nameAc':'activity2', 'advisor':'advisor2', 'date':'date2', 'type':'type2', 'des':'des2', 'file':'file2'},
            {'nameAc':'activity3', 'advisor':'advisor3', 'date':'date3', 'type':'type3', 'des':'des3', 'file':'file3'}]

@test.route('/')
def html():
	return render_template('testLoop.html', page = activity)

test.run(debug=True)
