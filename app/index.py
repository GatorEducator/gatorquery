import flask
from app import app


@app.route("/")
def index():
    """Render index.html"""
    return flask.render_template("index.html")


@app.route("/logout/")
def logout():
    """Execute the logout endpoint"""
    flask.session.pop("id", None)
    flask.session.pop("isTeacher", None)
    return flask.redirect("/")
