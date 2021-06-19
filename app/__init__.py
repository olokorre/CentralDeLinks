from flask import Flask
import db
from decouple import config


app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
BD = db.BancoDeDados(config('USER_DB'), config('PASSWD_DB'))

from .routes import aux, index, users, links
from .controllers import users, index, links