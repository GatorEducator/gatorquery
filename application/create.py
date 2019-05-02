""" Documentation needed """

from flask import render_template
from application import app


@app.route("/create")
def create_survey():
    """ Render the create_survey page """
    # pylint: disable=fixme
    # add a link system that has the user select
    # what type of element to add.  When a new element
    # is added, {% include %} it into the create.html
    # page by some means.

    return render_template("create.html")
