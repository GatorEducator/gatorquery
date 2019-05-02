""" Documentation needed """

import os
from flask import render_template, request
from application import app


poll_data = {
    "question": "Which web framework do you use?",
    "fields": ["Flask", "Django", "TurboGears", "web2py", "pylonsproject"],
}
filename = os.path.join("application", "data")
filename = os.path.join(filename, "data.txt")

# pylint: disable=cyclic-import
@app.route("/poll")
def poll():
    """ Documentation neede """
    vote = request.args.get("field")

    store_result(filename, vote)

    return render_template("multi-choice.html", data=poll_data)


# pylint: disable=redefined-outer-name
def store_result(filename, vote):
    """ Documentation needed """
    out = open(filename, "a")
    out.write(vote + "\n")
    out.close()
