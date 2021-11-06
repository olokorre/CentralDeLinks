from flask import session, request
from app import BD
from ..database import links, users

def delete_links(id):
    user = users.get_user(session.get('userID'))
    if not user: return {
        "message": "Não autenticado"
    }, 401
    try:
        links.delete_link(id, user[0])
        return {'message': 'ok' }
    except:
        return {
            "message": "Link não encontrado"
        }, 404

def share_links(id):
    try:
        BD.share_link(id, session.get('userID'), request.form['destinatario'])
        return {'messange': 'Link enviado para ' + request.form['destinatario'] + '!' }, 201
    except:
        return {'messange': request.form['destinatario'] + ' não foi reconhecido como usuário...' }, 404

def get_links():
    user = users.get_user(session.get('userID'))
    if not user: return {
        "message": "Não autenticado"
    }, 401
    link = links.get_links(user[0])
    return {
        "message": "Ok",
        "links": link
    }, 200

def save_link():
    user = users.get_user(session.get('userID'))
    if not user: return {
        "message": "Não autenticado"
    }, 401
    nome = request.form['nome']
    link = request.form['link']
    links.save_link(nome, link, user[0])
    return {
        "message": "OK"
    }, 200