""" Connection to the database """

import functools
import sqlite3
import flask

# from flask import g, session, escape
from application import app


DATABASE = "database.db"


def get_db():
    """ Retrieve the database """
    db = getattr(flask.g, "_database", None)
    if db is None:
        db = flask.g_database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
# pylint: disable=unused-argument
def close_connection(exception):
    """ Closes the connection to the database """
    db = getattr(flask.g, "_database", None)
    if db is not None:
        db.close()
