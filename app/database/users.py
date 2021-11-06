from app import BD

def get_user(user_nick):
    BD.mycursor.execute("select * from users where users.nick = '%s'" %user_nick)
    return BD.mycursor.fetchone()

def log_in(user_nick, user_passwd):
    BD.mycursor.execute("select * from users where users.nick = '%s' and users.passwd = '%s'" %(user_nick, user_passwd))
    return BD.mycursor.fetchone()