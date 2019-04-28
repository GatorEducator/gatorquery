""" Documentation needed """

import os
from flask import render_template, request

app = Flask(__name__)

poll_data = {
    "question": "Which web framework do you use?",
    "fields": ["Flask", "Django", "TurboGears", "web2py", "pylonsproject"],
}
filename = os.path.join("data", "data.txt")


@app.route("/poll")
def poll():
    """ Documentation needed """
    vote = request.args.get("field")

    out = open(filename, "a")
    out.write(vote + "\n")
    out.close()

    return render_template("thankyou.html", data=poll_data)
