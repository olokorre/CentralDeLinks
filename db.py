import mysql.connector
from decouple import config

class BancoDeDados(object):
	def __init__(self, user, passwd):
		self.mydb = mysql.connector.connect(user = user, passwd = passwd, db = config('DB')) # conecção com o banco de dados
		self.mycursor = self.mydb.cursor()

	def basic_request(self, user):
		try:
			self.mycursor.execute('select * from users')
			for i in self.mycursor:
				if user == i[0]: table = 'table_' + i[0]
			return table
		except mysql.connector.errors.OperationalError:
			self.mydb.rollback()
			self.basic_request(user)

	def user_check(self, nick, passwd):
		try:
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
		except mysql.connector.errors.OperationalError:
			self.mydb.rollback()
			self.user_check(nick, passwd)
	
	def create_user(self, nick, passwd):
		try:
			table = 'table_' + nick
			self.mycursor.execute('insert into users (nick, passwd, tables) value ("%s", "%s", "%s")' % (nick, passwd, table))
			self.mycursor.execute('create table %s (id int(191) primary key auto_increment, nome varchar(191), link varchar(191))' % (table))
			return True
		except mysql.connector.errors.OperationalError:
			self.mydb.rollback()
			self.create_user(nick, passwd)
		except:
			return False

	def request(self, user, passwd):
		try:
			if not self.user_check(user, passwd): return False
			table = self.basic_request(user)
			nome = []
			link = []
			_id = []
			self.mycursor.execute('select * from %s' % (table))
			for i in self.mycursor:
				nome.append(i[1])
				link.append(i[2])
				_id.append(i[0])
			return [nome, link, _id]
		except mysql.connector.errors.OperationalError:
			self.mydb.rollback()
			self.request(user, passwd)

	def send_data(self, user, passwd, nome, link):
		try:
			if not self.user_check(user, passwd): return False
			table = self.basic_request(user)
			self.mycursor.execute('insert into %s (nome, link) value ("%s", "%s")' % (table, nome, link))
			self.mydb.commit()
			return True 
		except mysql.connector.errors.OperationalError:
			self.mydb.rollback()
			self.send_data(user, passwd, nome, link)

	def get_profile(self, user):
		try:
			self.mycursor.execute('select bio from users where nick = "%s"' %user)
			return self.mycursor.fetchone()[0]
		except mysql.connector.errors.OperationalError:
			self.mydb.rollback()
			self.get_profile(user)

	def save_bio(self, bio, user):
		try:
			self.mycursor.execute('update users set bio = "%s" where nick = "%s"'%(bio, user))
			self.mydb.commit()
		except mysql.connector.errors.OperationalError:
			self.mydb.rollback()
			self.save_bio(user, bio)

	def delete_link(self, id, user):
		try:
			table = self.basic_request(user)
			self.mycursor.execute('delete from %s where id = %s' %(table, id))
			self.mydb.commit()
		except mysql.connector.errors.OperationalError:
			self.mydb.rollback()
			self.delete_link(id)

if __name__ == '__main__':
    mydb = mysql.connector.connect(user = config('USER_DB'), passwd = config('PASSWD_DB'))
    mycursor = mydb.cursor()
    mycursor.execute("create database %s" %config('DB'))
    mycursor.execute("use %s" %config('DB'))
    mycursor.execute("create table users (nick varchar(191) primary key, passwd varchar(191), bio text default 'Aqui, você pode falar um pouco sobre você :)', tables varchar(191))")

    print("Pronto!")