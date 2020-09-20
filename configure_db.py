import mysql.connector

user = input("Qual o nome do usuario MySQL?\n$ ")
passwd = input("Qual a senha desse usuario?\n$ ")

mydb = mysql.connector.connect(user = user, passwd = passwd)
mycursor = mydb.cursor()
mycursor.execute("create database Links")
mycursor.execute("use Links")
mycursor.execute("create table users (nick varchar(255) primary key, tables varchar(255))")

file_user = open('user.txt', 'w')
file_user.write(user + '\n' + passwd)
file_user.close()

print("Pronto!\nAgora você já pode executar o 'main.py' sem problemas, o banco de dados está pronto.")
