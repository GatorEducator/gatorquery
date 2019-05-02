""" Documentation needed """

from flask import render_template
from application import app


@app.route("/")
def root():
    """ Render the home page """
    return render_template("home.html")
