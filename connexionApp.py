# from flask_cors import CORS
from gevent import monkey
monkey.patch_all()

from flask import jsonify
from flask import current_app
from flask import request
from flask_cors import CORS
import flask_socketio
import connexion
from connexion.spec import Specification
from connexion.middleware.abstract import AbstractRoutingAPI
from connexion import FlaskApi
# This is in Connexion docs but doesn't seem to be a thing
# from asgi_framework import App
from connexion import ConnexionMiddleware
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware
# from connexion.resolver import RestyResolver
from connexion.resolver import RelativeResolver
import logging
import yaml

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

# API functions
#@app.route("/hello")
def hello():
  Log.info("Recieved get request")
  return jsonify({"message": "Hello, World!"})

def get_site_layout():
  return jsonify({"message": "Site Layout"})

# Flask app via Connexion
app = connexion.FlaskApp(__name__)
# This is supposed to work with connexion.App()
# app = ConnexionMiddleware(app)
flask_app = app.app

# NOTE: Will not work without this, despite Connexion docs stating CORS can't be added this way anymore.
CORS(flask_app)

import os
yaml_path = os.path.abspath('openapi.yaml')
print(f"Loading API from: {yaml_path}")

try:
  # app.add_api('openapi.yaml')
  app.add_api('openapi.yaml', resolver=RelativeResolver('connexionApp'))
  for rule in flask_app.url_map.iter_rules():
    print(f"Registered routes after add_api(): {rule} -> {rule.endpoint}")
  flask_app.config['DEBUG'] = True
  flask_app.debug = True
  Log.info("API successfully loaded.")
except Exception as e:
  Log.error(f"Error loading API: {e}")
  print(f"Error loading API: {e}")

# print(dir(app.middleware.apis))
# print(f"apis: {app.middleware.apis}")
for api in app.middleware.apis:
  #  print(f"API: {dir(api.specification)}")
  #  print(f"scheme: {api.specification.yaml_name}")
  main_api = FlaskApi(api.specification)
# print(f"MAIN API: {dir(main_api.blueprint)}")
flask_app.register_blueprint(main_api.blueprint)
print("**** Total routes: {}".format({len(list(app.app.url_map.iter_rules()))}))
print("**** API loaded with routes: {}".format(app.app.url_map))
# print(f"Config: {flask_app.config}")
# NOTE: This should create the same SPEC as is located in app.middleware
#api_test = Specification.load("/home/graham63/utility/code/connexionApp/openapi.yaml")
#print(f"spec: {api_test}")

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
socketio = flask_socketio.SocketIO(flask_app,
                                   cors_allowed_origins='*', async_mode='gevent')

with flask_app.app_context():
  current_app.config['socketio'] = socketio
  current_app.config['DEBUG'] = True

# api_url = "http://localhost:8000/v3.0.0/openapi.json"


# Methods for first bandaid attempt
# Load and parse the OpenAPI YAML file
def load_openapi_spec(spec_path='openapi.yaml'):
  with open(spec_path, 'r') as stream:
    try:
      return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)

# Dynamically create operation_function_map
def create_operation_function_map(spec, module_globals):
  op_func_map = {}

  for path, methods in spec['paths'].items():
    for method, operation in methods.items():
      operation_id = operation['operationId']
      print(f"operationID: {operation_id}")
      # Dynamically get the function from the current module by the operationId
      # print(f"Looking for function: {operation_id} in module_globals: {module_globals}")
      # function = getattr(module_globals, operation_id, None)
      function = module_globals.get(operation_id, None)
      if function is not None:
        op_func_map[operation_id] = function
      else:
        print(f"Warning: No function found for operationId '{operation_id}'")

  return op_func_map

# Register routes dynamically
def register_routes_from_openapi(app, spec, op_func_map):
  for path, methods in spec['paths'].items():
    for method, operation in methods.items():
      operation_id = operation['operationId']
      if operation_id in op_func_map:
        # Use app.route() to dynamically create routes
        app.route(path, methods=[method.upper()])(op_func_map[operation_id])

# Load the OpenAPI spec
# openapi_spec = load_openapi_spec()

# Dynamically create the operation_function_map by scanning the current module
# operation_function_map = create_operation_function_map(openapi_spec, globals())
# print(operation_function_map)

# Register the routes dynamically based on the OpenAPI spec
# register_routes_from_openapi(flask_app, openapi_spec, operation_function_map)

# Random attempt to make function to get openapi.json
# def get_openapi_as_json():
#  return print(json.dumps(openapi_spec, indent=2))

# SocketIO event handlers
@socketio.on('connect')
def handle_connect():
  print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
  print('Client disconnected')

@socketio.on('*')
def handle_events(event, data):
  print(f"Event: {event}, Data: {data}")

if __name__ == '__main__':
  # List registered routes (optional for debugging)
  def list_routes():
    import urllib.parse
    for rule in app.app.url_map.iter_rules():
      Log.info(f"{rule.endpoint} -> {rule}")

  list_routes()

  # Run server
  with flask_app.app_context():
    socketio = current_app.config['socketio']
    socketio.run(app.app, host='0.0.0.0', port=5000, debug=True)
  # socketio.run(app.app, host='0.0.0.0', port=5000, debug=True)
  # app.run()

