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

def query_db(query, args=(), one=False):
    """ Query the information in the database """
    cur = get_db().execute(query, args)
    returnval = cur.fetchall()
    cur.close()
    return (returnval[0] if returnval else None) if one else returnval
