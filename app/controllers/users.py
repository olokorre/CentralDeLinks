from app import app, BD
from flask import render_template, request, redirect, make_response
import hashlib, functions

def log_out():
    resp = make_response(render_template('login.html', dar = functions.dar()))
    resp.set_cookie('userID', 'None')
    resp.set_cookie('userpasswd', 'None')
    return resp

def create_user():
    nick = request.form['user']
    passwd = hashlib.md5(request.form['senha'].encode())
    if BD.create_user(nick, passwd.hexdigest()):
        resp = make_response(redirect('/'))
        resp.set_cookie('userID', nick)
        resp.set_cookie('userpasswd', passwd.hexdigest())
        return resp
    else: 
        return render_template(
            'error.html',
            erro = 'Esse usuario já existe...',
            url = '/login',
            action = "Entrar",
            dar = functions.dar()
        )

def log_in():
    nick = request.form['user']
    passwd = hashlib.md5(request.form['senha'].encode())
    if BD.user_check(nick, passwd.hexdigest()):
        resp = make_response(redirect('/'))
        resp.set_cookie('userID', nick)
        resp.set_cookie('userpasswd', passwd.hexdigest())
        return resp
    else:
        return render_template(
            'error.html', 
            erro = 'Usuario não existe ou senha incorreta...', 
            url = '/create',
            action = 'Registrar-se', 
            dar = functions.dar()
        )

def get_profile(view_user):
    user = request.cookies.get('userID')
    passwd = request.cookies.get('userpasswd')
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
    user = request.cookies.get('userID')
    passwd = request.cookies.get('userpasswd')
    if user == None or user == 'None': return redirect('/login')
    BD.save_bio(request.form['bio'], user)
    return { "messange": "ok" }