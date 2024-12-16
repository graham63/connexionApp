import connexion
from connexion.resolver import RelativeResolver
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware
from flask import jsonify
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

# Socketio event methods
@sio.event
async def socketioTest(sid, data):
  await sio.emit("broadcast", "Broadcast message from the server")
  print("******* Received message {}, from {}, emitted broadcast".format(data, sid))

@sio.event
async def connect(sid, environ):
  print(f"******** Client connected: {sid}")

# API functions
async def hello():
  return jsonify({"message": "Hello, World!"})

async def get_site_layout():
  return jsonify({"message": "Site Layout"})


# Server appplication method
async def app(scope, receive, send):
    if scope["type"] == "websocket" or scope["path"].startswith("/socket.io"):
        # Handle WebSocket and polling requests with Socket.IO
        await sio_asgi_app(scope, receive, send)
    else:
        # Handle REST API requests with Connexion
        with connexion_app.app.app_context():
          await connexion_app(scope, receive, send)

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, port=8080)

