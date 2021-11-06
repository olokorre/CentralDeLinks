from app import BD

def get_links(user_id):
    BD.mycursor.execute("select * from links where links.user_id = %s" %user_id)
    return BD.mycursor.fetchall()

def save_link(nome, link, user_id):
    BD.mycursor.execute("insert into links (nome, link, user_id) values ('%s', '%s', %s)" %(nome, link, user_id))
    BD.mydb.commit()

def delete_link(id, user_id):
    BD.mycursor.execute('delete from links where links.id = %s and links.user_id = %s' %(id, user_id))
    BD.mydb.commit()