import connexion
from connexion.resolver import RelativeResolver
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware
from flask import jsonify
from pathlib import Path


app = connexion.AsyncApp(__name__)
app.add_api('openapi.yaml', resolver=RelativeResolver('pureConnexion'))

app.add_middleware(
  CORSMiddleware,
  position=MiddlewarePosition.BEFORE_EXCEPTION,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# API functions
def hello():
    return jsonify({"message": "Hello, World!"})

def get_site_layout():
  return jsonify({"message": "Site Layout"})

if __name__ == '__main__':
    app.run(f"{Path(__file__).stem}:app", port=8080, log_level="debug")
