from flask import Flask
import db
from decouple import config

app = Flask(__name__)
BD = db.BancoDeDados(config('USER_DB'), config('PASSWD_DB'))

from .routes import aux, index, users
from .controllers import users, index