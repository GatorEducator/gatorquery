from application import app
from flask import Flask, render_template, url_for
from application import poll

@app.route('/')
def root():
    """ Render the home page """
    return render_template('home.html')
