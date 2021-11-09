from app import app, BD
from flask import render_template, request, redirect, make_response, session
import hashlib, functions
from ..database import users

def log_out():
    resp = make_response(render_template('login.html', dar = functions.dar()))
    session['userID'] = 'None'
    session['userpasswd'] = 'None'
    return resp

def create_user():
    nick = request.form['user']
    passwd = hashlib.md5(request.form['senha'].encode())
    try:
        user = users.create_user(nick, passwd.hexdigest())
        resp = make_response({
            "message": "ok"
        }, 201)
        session['userID'] = user[1]
        session['userpasswd'] = user[2]
        return resp
    except: 
        return {
            "message": "Usuário já existe..."
        }, 400

def log_in():
    nick = request.form['user']
    passwd = hashlib.md5(request.form['senha'].encode())
    user = users.log_in(nick, passwd.hexdigest())
    if user:
        resp = make_response({
            "message": "nice"
        }, 200)
        session['userID'] = user[1]
        session['userpasswd'] = user[2]
        return resp
    else:
        return {
            "message": "Usuário e senha não conferem..."
        }, 400

def get_profile(view_user):
    user = users.get_user(session.get('userID'))
    view_user = users.get_user(view_user)
    if not user: return redirect('/login')
    return render_template(
        'profile.html',
        dar = functions.dar(),
        user = user[1],
        user_profile = view_user[1],
        bio_user = view_user[3]
    )

def save_bio():
    user = session.get('userID')
    passwd = session.get('userpasswd')
    if user == None or user == 'None': return redirect('/login')
    BD.save_bio(request.form['bio'], user)
    return { "messange": "ok" }

def get_select_data():
    result = [ i[0] for i in users.search(request.args.get('term'))]
    return {
        "items": result
    }