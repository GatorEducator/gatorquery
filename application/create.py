from application import app
from flask import Flask, render_template

@app.route('/create')
def create_survey():
    """ Render the create_survey page """

    # TODO: add a link system that has the user select
    # what type of element to add.  When a new element
    # is added, {% include %} it into the create.html
    # page by some means.

    return render_template('create.html')
