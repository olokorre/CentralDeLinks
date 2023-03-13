from app import app
from flask import request
from ..controllers import links

@app.route('/links/<id>', methods=['DELETE'])
def delete_links(id):
    return links.delete_links(id)

@app.route('/links', methods=['GET', 'POST'])
def get_links():
    if request.method == 'GET': return links.get_links()
    return links.save_link()

@app.route('/share/<id>', methods=['POST'])
def share_link(id):
    return links.share_links(id)
