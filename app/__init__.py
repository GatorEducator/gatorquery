""" Application package initializer """
import flask
from . import index
from . import db_connect
from . import login
from . import students
from . import teachers

# main flask instance
app = flask.Flask(__name__)
