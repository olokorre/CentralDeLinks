from app import BD
from flask import render_template, request, redirect
import functions

def create_link():
    user = request.cookies.get('userID')
    passwd = request.cookies.get('userpasswd')
    if BD.send_data(user, passwd, request.form['nome'], request.form['link']): return redirect('/')
    return render_template(
        'error.html',
        erro = 'Senha inválida!',
        url = '/login',
        action = 'Voltar',
        dar = functions.dar()
    )

def get_liks():
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
        'index.html',
        dar = functions.dar(), 
        nome = request_db[0],
        link = request_db[1],
        tam = len(request_db[0]),
        user = user
    )