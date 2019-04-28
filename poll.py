from flask import Flask, render_template, request
import os
app = Flask(__name__)

filename = "data.txt"

poll_data = {
   'question' : 'What is your favorite color?',
   'fields'   : ['Blue', 'Yellow', 'Pink', 'Red', 'Sky Blue', 'Purple']
}

@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)

@app.route('/poll')
def poll():
    vote = request.args.get('field')

    out = open(filename, 'a')
    out.write( vote + '\n' )
    out.close()

    return render_template('thankyou.html', data=poll_data)

@app.route('/long_answer')
def long_answer():
	

if __name__ == "__main__":
    app.run(debug=True)
