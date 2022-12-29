from app import app
from ..controllers import index
from flask import request

@app.route('/', methods = ('GET', 'POST'))
def main():
	if request.method == 'GET': return index.get_liks()
	elif request.method == 'POST': return index.create_link()
