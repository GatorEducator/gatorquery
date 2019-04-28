""" Documentation needed """

import os
from flask import render_template
from application import app


poll_data = {
    "question": "Which web framework do you use?",
    "fields": ["Flask", "Django", "TurboGears", "web2py", "pylonsproject"],
}
# Unsure if this is correct file path, but necessary to pass pylint
filename = os.path.join("application", "data")
filename = os.path.join(filename, "data.txt")

@app.route("/results")
def show_results():
    """ Documentation needed """
    votes = {}
    for f in poll_data["fields"]:
        votes[f] = 0

    f = open(filename, "r")
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1

    return render_template("results.html", data=poll_data, votes=votes)
