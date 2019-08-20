# flask is the framework here, while Flask is a Python class datatype
from flask import Flask

# to create an instance of the Flask class for our web app
app = Flask(__name__)

from firstapp import routes
