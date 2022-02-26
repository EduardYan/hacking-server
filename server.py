"""
This file have some
configurations or settings
for the server.
For execute the server execute
the file 'index.py'

"""


from flask import Flask
from routes.server_routes import myroutes


# creating the server
server = Flask(__name__)


# using the routes
server.register_blueprint(myroutes)
