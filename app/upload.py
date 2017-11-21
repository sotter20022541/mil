from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import os
from shutil import copyfile

from pathlib import Path
from flask import Flask, render_template, request
from werkzeug import secure_filename

import shutil

test = Flask(__name__)


@test.route('/')
def html():
	return render_template('upload.html')

@test.route('/getfile', methods=['POST'])
def getfile():

	ffile = request.form['file']
	print(ffile)

	copy = 'Copy' + str(ffile)
	copyto = 'C:/Users/Pop PerZz/Desktop/' + str(copy)

	shutil.copy(ffile, copyto)

test.run(debug=True)
