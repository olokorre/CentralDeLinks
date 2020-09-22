import mysql.connector

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

if __name__ == '__main__':
    user = input("Qual o nome do usuario MySQL?\n$ ")
    passwd = input("Qual a senha desse usuario?\n$ ")

    mydb = mysql.connector.connect(user = user, passwd = passwd)
    mycursor = mydb.cursor()
    mycursor.execute("create database Links")
    mycursor.execute("use Links")
    mycursor.execute("create table users (nick varchar(255) primary key, passwd varchar(255), tables varchar(255))")

    file_user = open('user.txt', 'w')
    file_user.write(user + '\n' + passwd)
    file_user.close()

    print("Pronto!\nAgora você já pode executar o 'main.py' sem problemas, o banco de dados está pronto.")