from flask import Flask, render_template, send_from_directory, request, redirect # dependencias do Flask
import mysql.connector # dependencias do MySQL
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

	def user_check(self, nick):
		self.mycursor.execute('select * from users')
		list_of_users = []
		for i in self.mycursor:
			list_of_users.append(i[0])
		if nick in list_of_users: return True
		return False

	def request(self, user):
		self.mycursor.execute('select * from users')
		for i in self.mycursor:
			print(i[0], user)
			if user == i[0]: table = i[1]
		self.mycursor.execute('select * from %s' % (table))
		return self.mycursor

	def enviar(self, user, nome, link):
		self.mycursor.execute('select * from users')
		for i in self.mycursor:
			if user == i[0]: table = i[1]
		self.mycursor.execute('insert into %s (nome, link) value ("%s", "%s")' % (table, nome, link))
		self.mydb.commit()

def user_db():
	user = open('user.txt', 'r')
	return_user = user.readlines()
	user.close()
	return return_user

user = user_db()
saudacao = Saudacao()
BD = BancoDeDados(user[0], user[1])
user = "Entrar"

@app.route('/', methods = ('GET', 'POST')) # rota principal
def index():
	nome = []
	link = []
	if request.method == 'GET':
		if user == "Entrar": return redirect('/user_mananger')
		linksDis = BD.request(user)
		for i in linksDis: # agrupar os nomes e os links em suas respectivas listas
			nome.append(i[1])
			link.append(i[2])
		return render_template('index.html', dar = saudacao.dar(), nome = nome, link = link, tam = len(nome), user = user) # renderiza e entrega o templete ao cliente
	if request.method == 'POST': # encarregado de receber os novos links
		BD.enviar(user, request.form['nome'], request.form['link'])
		return redirect('/')

@app.route('/user_mananger', methods = ('GET', 'POST'))
def user_mananger():
	global user
	if request.method == 'GET': return render_template('login.html', dar = saudacao.dar())
	elif request.method == 'POST':
		nick = request.form['user']
		if BD.user_check(nick): user = nick
		else: user = "Entrar"
		return redirect('/')
	return '404'

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