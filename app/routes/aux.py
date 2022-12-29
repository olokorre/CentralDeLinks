from app import app
from flask import send_from_directory

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('static/css', path)

@app.route('/image/<path:path>')
def send_image(path):
	return send_from_directory('static/image', path)

@app.route('/fonts/<path:path>')
def send_font(path):
	return send_from_directory('static/fonts', path)
