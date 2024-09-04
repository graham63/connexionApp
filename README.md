# connexionApp
Basic Python server example using Connexion with Flask Socketio.

`connexionApp.py` uses Flask Socketio. `minApp.py` runs the connexion app directly. 
`curl http://localhost:8000/hello` returns the expected response from minApp.py,
although the url_map is not populated correctly.
