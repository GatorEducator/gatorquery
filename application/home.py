from application import app
from flask import Flask, render_template

@app.route('/')
def home_page():
    """ Render the home page """
    return render_template('home.html')
