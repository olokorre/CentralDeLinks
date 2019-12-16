from flask import Flask, render_template, send_from_directory, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods = ('GET', 'POST'))
def index():
	nome = []
	link = []
	mydb = mysql.connector.connect(user = "olokorre", passwd = "Linux@290")
	mycursor = mydb.cursor()
	mycursor.execute("use Links")
	mycursor.execute("select * from links")
	for i in mycursor:
		nome.append(i[1])
		link.append(i[2])
	if request.method == 'POST':
		n = request.form['nome']
		l = request.form['link']
		mycursor.execute('insert into links (nome, link) value ("%s", "%s")' % (n, l))
		mydb.commit()
		return redirect('/')
	now = datetime.now()
	if now.hour >= 6 and now.hour < 12: dar = "Bom Dia!"
	elif now.hour >= 12 and now.hour < 19: dar = "Boa Tarde!"
	else: dar = "Boa Noite!"
	return render_template('index.html', dar = dar, nome = nome, link = link, tam = len(nome))

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