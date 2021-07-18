from flask import session, request
from app import BD

def delete_links(id):
    BD.delete_link(id, session.get('userID'))
    return {'messange': 'ok' }

def share_links(id):
    try:
        BD.share_link(id, session.get('userID'), request.form['destinatario'])
        return {'messange': 'Link enviado para ' + request.form['destinatario'] + '!' }, 201
    except:
        return {'messange': request.form['destinatario'] + ' não foi reconhecido como usuário...' }, 404