""" Connection to the database """

import functools
import sqlite3
import flask

# from flask import g, session, escape
from application import app


DATABASE = "database.db"
