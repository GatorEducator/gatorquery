""" File to take the user to the login page """

import flask
from application import app

# LOGIN THE USER
@app.route("/login")
def login():
    """ Render the login page """
    return flask.render_template("login.html")


# LOGIN THE USER
@app.route("/register/")
def register():
    """ Render the register page """
    return flask.render_template("register.html")
