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