from app import app
from flask import render_template, request
from ..controllers import users
import functions

@app.route('/login', methods = ('GET', 'POST'))
def login():
	if request.method == 'GET': return users.log_out()
	elif request.method == 'POST': return users.log_in()

@app.route('/create', methods = ('GET', 'POST'))
def create():
	if request.method == 'GET': return render_template('create.html', dar = functions.dar())
	elif request.method == 'POST': return users.create_user()

@app.route('/profile/<user>', methods = ('GET', 'POST'))
def prifile(user):
	if request.method == 'GET': return users.get_profile(user)
	return users.save_bio()

@app.route('/profile')
def get_select_data():
	return users.get_select_data()