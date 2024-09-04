from gevent import monkey
monkey.patch_all()

import connexion
from flask_socketio import SocketIO
from flask import jsonify
from connexion.resolver import RelativeResolver

app = connexion.FlaskApp(__name__, specification_dir='.')
app.add_api('openapi.yaml', resolver=RelativeResolver('connexionApp'))

socketio = SocketIO(app.app, cors_allowed_origins="*", async_mode='gevent')

# API functions
def hello():
    return jsonify({"message": "Hello, World!"})

def get_site_layout():
  return jsonify({"message": "Site Layout"})

if __name__ == '__main__':
    socketio.run(app.app, host='0.0.0.0', port=8000, debug=True)
