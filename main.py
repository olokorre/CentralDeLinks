from flask import Flask, render_template, send_from_directory, request, redirect # dependencias do Flask
import mysql.connector # dependencias do MySQL
from datetime import datetime # dependencias do datetime

app = Flask(__name__)

class Saudacao(object):
	def dar(self):
		now = datetime.now() # consulta a hora do sistema operacional do servidor
		if now.hour >= 6 and now.hour < 12: dar = "Bom Dia!"
		elif now.hour >= 12 and now.hour < 19: dar = "Boa Tarde!"
		else: dar = "Boa Noite!"
		return dar

class BancoDeDados(object):
	def __init__(self, user, passwd):
		self.mydb = mysql.connector.connect(user = user, passwd = passwd) # conecção com o banco de dados
		self.mycursor = self.mydb.cursor()
		self.mycursor.execute("use Links")
	
	def links(self):
		self.mycursor.execute("select * from links")
		return self.mycursor
	
	def enviar(self, nome, link):
		self.mycursor.execute('insert into links (nome, link) value ("%s", "%s")' % (nome, link))
		self.mydb.commit()

saudacao = Saudacao()
BD = BancoDeDados("olokorre", "Linux@290")

@app.route('/', methods = ('GET', 'POST')) # rota principal
def index():
	nome = []
	link = []
	linksDis = BD.links()
	for i in linksDis: # agrupar os nomes e os links em suas respectivas listas
		nome.append(i[1])
		link.append(i[2])
	if request.method == 'POST': # encarregado de receber os novos links
		BD.enviar(request.form['nome'], request.form['link'])
		return redirect('/')
	
	return render_template('index.html', dar = saudacao.dar(), nome = nome, link = link, tam = len(nome)) # renderiza e entrega o templete ao cliente

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