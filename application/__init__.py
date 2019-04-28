""" Application package initializer """
import flask
from . import login
from . import poll
from . import create
from . import home

# main flask instance
app = flask.Flask(__name__)
