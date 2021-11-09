from app import BD

def get_user(user_nick):
    BD.mycursor.execute("select * from users where users.nick = '%s'" %user_nick)
    return BD.mycursor.fetchone()

def log_in(user_nick, user_passwd):
    BD.mycursor.execute("select * from users where users.nick = '%s' and users.passwd = '%s'" %(user_nick, user_passwd))
    return BD.mycursor.fetchone()

def create_user(nick, passwd):
    BD.mycursor.execute("insert into users (nick, passwd) values ('%s', '%s')" %(nick, passwd))
    BD.mydb.commit()
    BD.mycursor.execute("select * from users where users.nick = '%s' and users.passwd = '%s'" %(nick, passwd))
    return BD.mycursor.fetchone()


def search(term):
    BD.mycursor.execute("select users.nick from users where users.nick like '%{}%'".format(term))
    return BD.mycursor.fetchall()