""" Application package initializer """
import flask

# main flask instance
app = flask.Flask(__name__)

#from . import results
#from . import login
#from . import poll
from . import home
