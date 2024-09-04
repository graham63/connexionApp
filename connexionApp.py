# from flask_cors import CORS
from gevent import monkey
monkey.patch_all()

from flask import jsonify
from flask import current_app
import flask_socketio
import connexion
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware
# from connexion.resolver import RestyResolver
from connexion.resolver import RelativeResolver
import logging

import yaml
with open('openapi.yaml', 'r') as f:
  try:
    yaml.safe_load(f)
    print("YAML loaded successfully.")
  except yaml.YAMLError as e:
    print(f"YAML parsing error: {e}")
        
# Log file/console stuff
Log = logging.getLogger(__name__)
Log.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
Log.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
Log.addHandler(console_handler)

# Log registered routes
def list_routes():
    import urllib.parse

    Log.info(f"Total routes: {len(list(app.app.url_map.iter_rules()))}")

    max_endpoint_length = max(len(rule.endpoint) for rule in app.app.url_map.iter_rules())
    max_methods_length = max(len(','.join(rule.methods)) for rule in app.app.url_map.iter_rules())

    # Log URL map
    url_map_lines = sorted(
        urllib.parse.unquote(f"{rule.endpoint:{max_endpoint_length}} {','.join(rule.methods):{max_methods_length}} {rule}")
        for rule in app.app.url_map.iter_rules()
    )

    for line in url_map_lines:
        Log.info("***** URL MAP*****: {}".format(line))
        
# Flask app via Connexion
app = connexion.FlaskApp(__name__)

import os
yaml_path = os.path.abspath('openapi.yaml')
print(f"Loading API from: {yaml_path}")

try:
  #app.add_api('openapi.yaml', resolver=RestyResolver('connexionApp'))
  app.add_api('openapi.yaml', resolver=RelativeResolver('connexionApp'))
  Log.info("API successfully loaded.")
except Exception as e:
  Log.error(f"Error loading API: {e}")
  print(f"Error loading API: {e}")

# add CORS support
app.add_middleware(
  CORSMiddleware,
  position=MiddlewarePosition.BEFORE_EXCEPTION,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Initialize Flask-SocketIO
socketio = flask_socketio.SocketIO(app.app,
                                   cors_allowed_origins='*',
                                   async_mode='gevent')

with app.app.app_context():
    current_app.config['socketio'] = socketio
    
# API functions 
@app.route("/hello")
def hello():
  return jsonify({"message": "Hello, World!"})

def get_site_layout():
  return jsonify({"message": "Site Layout"})

# SocketIO event handlers
@socketio.on('connect')
def handle_connect():
  print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
  print('Client disconnected')

if __name__ == '__main__':
    list_routes()
    
    # Run server
    with app.app.app_context():
      socketio = current_app.config['socketio']
      socketio.run(app.app, host='0.0.0.0', port=8000, debug=True)
    #socketio.run(app.app, host='0.0.0.0', port=8000, debug=True)
    # app.run()

