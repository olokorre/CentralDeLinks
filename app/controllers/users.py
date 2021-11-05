from app import app, BD
from flask import render_template, request, redirect, make_response, session
import hashlib, functions

def log_out():
    resp = make_response(render_template('login.html', dar = functions.dar()))
    session['userID'] = 'None'
    session['userpasswd'] = 'None'
    return resp

def create_user():
    nick = request.form['user']
    passwd = hashlib.md5(request.form['senha'].encode())
    if BD.create_user(nick, passwd.hexdigest()):
        resp = make_response(redirect('/'))
        session['userID'] = nick
        session['userpasswd'] = passwd.hexdigest()
        return resp
    else: 
        return {
            "message": "Usuário já existe..."
        }, 400

def log_in():
    nick = request.form['user']
    passwd = hashlib.md5(request.form['senha'].encode())
    if BD.user_check(nick, passwd.hexdigest()):
        resp = make_response(redirect('/'))
        session['userID'] = nick
        session['userpasswd'] = passwd.hexdigest()
        return resp
    else:
        return {
            "message": "Usuário e senha não conferem..."
        }, 400

def get_profile(view_user):
    user = session['userID']
    passwd = session['userpasswd']
    if user == None or user == 'None': return redirect('/login')
    request_db = BD.request(user, passwd)
    if request_db == False:
        return render_template(
            'error.html',
            erro = 'Senha inválida!',
            url = '/login',
            action = 'Voltar',
            dar = functions.dar()
        )
    return render_template(
        'profile.html',
        dar = functions.dar(),
        user = user,
        user_profile = view_user,
        bio_user = BD.get_profile(view_user)
    )

def save_bio():
    user = session.get('userID')
    passwd = session.get('userpasswd')
    if user == None or user == 'None': return redirect('/login')
    BD.save_bio(request.form['bio'], user)
    return { "messange": "ok" }