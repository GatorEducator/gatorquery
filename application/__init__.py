""" Application package initializer """

import flask

# main flask instance
app = flask.Flask(__name__)

# find a way to ignore pylint errors
# these have to be here.
from . import login
from . import poll
from . import create
from . import home
