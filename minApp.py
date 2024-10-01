# from gevent import monkey
# monkey.patch_all()

# from flask_socketio import SocketIO
from flask import jsonify
import connexion
# from connexion.resolver import RestyResolver
from connexion.resolver import RelativeResolver
from connexion.middleware.routing import RoutingMiddleware
from pathlib import Path
app = connexion.FlaskApp(__name__)
#app.add_api('openapi.yaml', resolver=RestyResolver('minApp'))
app.add_api('openapi.yaml')
app.app.config['DEBUG'] = True

# app.add_middleware(
#     RoutingMiddlware,
    
# )

#socketio = SocketIO(app.app, cors_allowed_origins="*", async_mode='gevent')

# API functions
def hello():
    return jsonify({"message": "Hello, World!"})

def get_site_layout():
  return jsonify({"message": "Site Layout"})

if __name__ == '__main__':
    print("**** Total routes: {}".format({len(list(app.app.url_map.iter_rules()))}))
    print("**** API loaded with routes: {}".format(app.app.url_map))
    for attribute in dir(app):
        print("**** App: {}".format(getattr(app, attribute)))
    print("***** Blueprint *****: {}".format(app.app.blueprints))
    # socketio.run(app.app, host='0.0.0.0', port=8000, debug=True)
    app.run(f"{Path(__file__).stem}:app", port=8080, log_level="debug")
