from flask import request

def delete_links(id):
    return {'message': 'ok' }

def share_links(id):
    return {'messange': 'Link enviado para ' + request.form['destinatario'] + '!' }, 201

def get_links():
    return {
        "message": "Ok",
        "links": []
    }, 200

def save_link():
    return {
        "message": "OK"
    }, 200
