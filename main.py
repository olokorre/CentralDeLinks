from flask import Flask, render_template, send_from_directory, request, redirect, make_response
import mysql.connector, hashlib, db, functions
from datetime import datetime

app = Flask(__name__)

user = functions.user_db()
BD = db.BancoDeDados(user[0], user[1])

@app.route('/', methods = ('GET', 'POST'))
def index():
	user = request.cookies.get('userID')
	passwd = request.cookies.get('userpasswd')
	if request.method == 'GET':
		if user == None or user == 'None': return redirect('/login')
		request_db = BD.request(user, passwd)
		if request_db == False:
			return render_template('error.html',
			erro = 'Senha inválida!',
			url = '/login',
			action = 'Voltar',
			dar = functions.dar())
		return render_template('index.html',
			dar = functions.dar(), 
			nome = request_db[0],
			link = request_db[1],
			tam = len(request_db[0]),
			user = user)
	if request.method == 'POST':
		if BD.send_data(user, passwd, request.form['nome'], request.form['link']): return redirect('/')
		return render_template('error.html',
			erro = 'Senha inválida!',
			url = '/login',
			action = 'Voltar',
			dar = functions.dar())

@app.route('/login', methods = ('GET', 'POST'))
def login():
	if request.method == 'GET':
		resp = make_response(render_template('login.html', dar = functions.dar()))
		resp.set_cookie('userID', 'None')
		resp.set_cookie('userpasswd', 'None')
		return resp
	elif request.method == 'POST':
		nick = request.form['user']
		passwd = hashlib.md5(request.form['senha'].encode())
		if BD.user_check(nick, passwd.hexdigest()):
			resp = make_response(redirect('/'))
			resp.set_cookie('userID', nick)
			resp.set_cookie('userpasswd', passwd.hexdigest())
			return resp
		else:
			return render_template('error.html', 
				erro = 'Usuario não existe...', 
				url = '/create', 
				action = 'Registrar-se', 
				dar = functions.dar())

@app.route('/create', methods = ('GET', 'POST'))
def create():
	if request.method == 'GET': return render_template('create.html', dar = functions.dar())
	elif request.method == 'POST':
		nick = request.form['user']
		passwd = hashlib.md5(request.form['senha'].encode())
		if BD.create_user(nick, passwd.hexdigest()):
			resp = make_response(redirect('/'))
			resp.set_cookie('userID', nick)
			resp.set_cookie('userpasswd', passwd.hexdigest())
			return resp
		else: return render_template('error.html', 
			erro = 'Esse usuario já existe...', 
			url = '/login', 
			action = "Entrar", 
			dar = functions.dar())

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('static/css', path)

@app.route('/image/<path:path>')
def send_image(path):
	return send_from_directory('static/image', path)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)