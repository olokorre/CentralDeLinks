import mysql.connector
from decouple import config

class BancoDeDados(object):
	def __init__(self, user, passwd):
		self.mydb = mysql.connector.connect(user = user, passwd = passwd, db = config('DB')) # conecção com o banco de dados
		self.mycursor = self.mydb.cursor()

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
			self.mycursor.execute('create table %s (id int(191) primary key auto_increment, nome varchar(191), link varchar(191))' % (table))
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

	def get_profile(self, user):
		self.mycursor.execute('select bio from users where nick = "%s"' %user)
		return self.mycursor.fetchone()[0]

	def save_bio(self, bio, user):
		print(bio)
		self.mycursor.execute('update users set bio = "%s" where nick = "%s"'%(bio, user))
		self.mydb.commit()

if __name__ == '__main__':
    mydb = mysql.connector.connect(user = config('USER_DB'), passwd = config('PASSWD_DB'))
    mycursor = mydb.cursor()
    mycursor.execute("create database %s" %config('DB'))
    mycursor.execute("use %s" %config('DB'))
    mycursor.execute("create table users (nick varchar(191) primary key, passwd varchar(191), bio text default 'Aqui, você pode falar um pouco sobre você :)', tables varchar(191))")

    print("Pronto!")