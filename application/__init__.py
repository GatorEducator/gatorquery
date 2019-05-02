""" Application package initializer """

import flask

# main flask instance
app = flask.Flask(__name__)

# pylint: disable=wrong-import-position
from . import login

# pylint: disable=wrong-import-position
from . import poll

# pylint: disable=wrong-import-position
from . import create

# pylint: disable=wrong-import-position
from . import home
