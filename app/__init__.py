from flask import Flask
import db
from decouple import config

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
BD = db.BancoDeDados(config('USER_DB'), config('PASSWD_DB'))

from .routes import aux, index, users, links
from .controllers import users, index, links