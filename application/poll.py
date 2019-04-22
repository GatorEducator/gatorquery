from application import app
from flask import Flask, render_template, request, url_for
import os

poll_data = {
   'question' : 'Which web framework do you use?',
   'fields'   : ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject']
}
filename = os.path.join("application", "data")
filename = os.path.join(filename, "data.txt")

@app.route('/poll')
def poll():
    vote = request.args.get('field')

    store_result(filename, vote)

    return render_template('multi-choice.html', data=poll_data)

def store_result(filename, vote):
        out = open(filename, 'a')
        out.write( vote + '\n' )
        out.close()
