from datetime import datetime

def dar():
	now = datetime.now() # consulta a hora do sistema operacional do servidor
	if now.hour >= 6 and now.hour < 12: dar = "bom dia!"
	elif now.hour >= 12 and now.hour < 19: dar = "boa tarde!"
	else: dar = "boa noite!"
	return dar

def user_db():
	user = open('user.txt', 'r')
	return_user = user.readlines()
	user.close()
	return return_user
