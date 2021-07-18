from app import app
from ..controllers import links

@app.route('/links/<id>', methods=['DELETE'])
def delete_links(id):
    return links.delete_links(id)

@app.route('/share/<id>', methods=['POST'])
def share_link(id):
    return links.share_links(id)