from flask import session
from app import BD

def delete_links(id):
    BD.delete_link(id, session.get('userID'))
    return {'messange': 'ok' }