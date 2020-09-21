from flask import Flask, render_template, send_from_directory, request, redirect, make_response
import mysql.connector # dependencias do MySQL
import hashlib
from datetime import datetime # dependencias do datetime

app = Flask(__name__)

class Saudacao(object):
	def dar(self):
		now = datetime.now() # consulta a hora do sistema operacional do servidor
		if now.hour >= 6 and now.hour < 12: dar = "bom dia!"
		elif now.hour >= 12 and now.hour < 19: dar = "boa tarde!"
		else: dar = "boa noite!"
		return dar

class BancoDeDados(object):
	def __init__(self, user, passwd):
		self.mydb = mysql.connector.connect(user = user, passwd = passwd) # conecção com o banco de dados
		self.mycursor = self.mydb.cursor()
		self.mycursor.execute("use Links")

	def basic_request(self, user):
		self.mycursor.execute('select * from users')
		for i in self.mycursor:
			if user == i[0]: table = 'table_' + i[0]
		return table

	def user_check(self, nick, passwd):
		self.mycursor.execute('select * from users')
		list_of_users = []
		list_passwd = []
		for i in self.mycursor:
			list_of_users.append(i[0])
			list_passwd.append(i[1])
		for i in list_of_users:
			for l in list_passwd:
				if nick == i and passwd == l: return True
		return False
	
	def create_user(self, nick, passwd):
		try:
			table = 'table_' + nick
			self.mycursor.execute('insert into users (nick, passwd, tables) value ("%s", "%s", "%s")' % (nick, passwd, table))
			self.mycursor.execute('create table %s (id int(255) primary key auto_increment, nome varchar(255), link varchar(255))' % (table))
			return True
		except:
			return False

	def request(self, user, passwd):
		if not self.user_check(user, passwd): return False
		table = self.basic_request(user)
		nome = []
		link = []
		self.mycursor.execute('select * from %s' % (table))
		for i in self.mycursor:
			nome.append(i[1])
			link.append(i[2])
		return [nome, link]

	def send_data(self, user, passwd, nome, link):
		if not self.user_check(user, passwd): return False
		table = self.basic_request(user)
		self.mycursor.execute('insert into %s (nome, link) value ("%s", "%s")' % (table, nome, link))
		self.mydb.commit()
		return True

def user_db():
	user = open('user.txt', 'r')
	return_user = user.readlines()
	user.close()
	return return_user

user = user_db()
saudacao = Saudacao()
BD = BancoDeDados(user[0], user[1])

@app.route('/', methods = ('GET', 'POST')) # rota principal
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
			dar = saudacao.dar())
		return render_template('index.html',
			dar = saudacao.dar(), 
			nome = request_db[0],
			link = request_db[1],
			tam = len(request_db[0]),
			user = user) # renderiza e entrega o templete ao cliente
	if request.method == 'POST': # encarregado de receber os novos links
		if BD.send_data(user, passwd, request.form['nome'], request.form['link']): return redirect('/')
		return render_template('error.html',
			erro = 'Senha inválida!',
			url = '/login',
			action = 'Voltar',
			dar = saudacao.dar())

@app.route('/login', methods = ('GET', 'POST'))
def login():
	if request.method == 'GET':
		resp = make_response(render_template('login.html', dar = saudacao.dar()))
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
				dar = saudacao.dar())

@app.route('/create', methods = ('GET', 'POST'))
def create():
	if request.method == 'GET': return render_template('create.html', dar = saudacao.dar())
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
			dar = saudacao.dar())

# rotas auxiliares
@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('static/css', path)

@app.route('/image/<path:path>')
def send_image(path):
	return send_from_directory('static/image', path)

# inicializador
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)