""" Documentation needed """

from flask import render_template
from application import app

# pylint: disable=cyclic-import
@app.route("/")
def root():
    """ Render the home page """
    return render_template("home.html")
