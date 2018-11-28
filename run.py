from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import os

app = Flask(__name__)

usernames = []
riddles = {} # including answers
user_answers = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    '''Landing page with form to submit username'''
    if request.method == 'POST':
        usernames.append(request.form['username'])
        return redirect(request.form['username'])
    return render_template('index.html')







if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),           
            debug=True)