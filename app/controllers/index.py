from app import BD
from flask import render_template, request, redirect, session
import functions
from ..database import users, links

def create_link():
    user = session.get('userID')
    passwd = session.get('userpasswd')
    if BD.send_data(user, passwd, request.form['nome'], request.form['link']): return redirect('/')
    return render_template(
        'error.html',
        erro = 'Senha inválida!',
        url = '/login',
        action = 'Voltar',
        dar = functions.dar()
    )

def get_liks():
    nick = session.get('userID')
    passwd = session.get('userpasswd')
    user = users.log_in(nick, passwd)
    if not user: return redirect('/login')
    link = links.get_links(user[0])
    return render_template(
        'index.html',
        dar = functions.dar(),
        user = user[1]
    )