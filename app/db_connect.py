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


def insert_db(query, args=()):
    """ Insert queries into the database """
    db = get_db()
    db.execute(query, args)
    db.commit()


def validate_student(func):
    """ Checks that the user trying to login is a student """

    @functools.wraps(func)
    def f(*args, **kwds):
        if "isTeaher" not in flask.session:
            return flask.redirect("/")
        if flask.session["isTeacher"] == 1:
            return flask.redirect("/teachers/")
        return func(*args, **kwds)

    return f


def validate_teacher(func):
    """ Checks that the user trying to login is a teacher """

    @functools.wraps(func)
    def f(*args, **kwds):
        if "isTeacher" not in flask.session:
            return flask.redirect("/")
        if flask.session["isTeacher"] == 0:
            return flask.redirect("/students/")
        return func(*args, **kwds)

    return f
