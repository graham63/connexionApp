import connexion
from connexion.resolver import RelativeResolver
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.wsgi import WSGIMiddleware
from flask import jsonify
from pathlib import Path
import socketio

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
sio_asgi_app = socketio.ASGIApp(sio)
connexion_app = connexion.App(__name__)
connexion_app.add_api('openapi.yaml', resolver=RelativeResolver('connexionServer'))

connexion_app.add_middleware(
  CORSMiddleware,
  position=MiddlewarePosition.BEFORE_EXCEPTION,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# combined_app = WSGIMiddleware(connexion_app)
# print(dir(connexion_app.app))
#print(dir(sio_asgi_app))
#sio.attach(connexion_app.app)

# API functions
async def hello():
    return jsonify({"message": "Hello, World!"})

async def get_site_layout():
  return jsonify({"message": "Site Layout"})

async def app(scope, receive, send):
    print("Called APP")
    if scope["type"] == "websocket" or scope["path"].startswith("/socket.io"):
        # Handle WebSocket and polling requests with Socket.IO
        await sio_asgi_app(scope, receive, send)
    else:
        # Handle REST API requests with Connexion
        print("CONNEXION APP")
        with connexion_app.app.app_context():
          await connexion_app(scope, receive, send)
        
#if __name__ == '__main__':
  # connexion_app.run(f"{Path(__file__).stem}:app", port=8080, log_level="debug")
  
