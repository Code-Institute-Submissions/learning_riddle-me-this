from flask import Flask
import json
from flask import redirect
from flask import render_template
from flask import request
import os

app = Flask(__name__)

usernames = []
user_answers = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Landing page with form to submit username
    """
    if request.method == 'POST':
        username = request.form['username']
        if username not in usernames:
            usernames.append(username)
            print(username)
        return redirect('riddle')
    return render_template('index.html')


@app.route('/<username>')
def user(username):
    return username


@app.route('/print_users')
def print_users():
    all_users = ''
    for user in usernames:
        all_users += user + ' '
    return all_users


def read_riddlesjson():
    with open('riddles.json', 'r', encoding='utf-8') as f:
        riddles = json.loads(f.read())
    return riddles   


def get_riddle(riddles):
    if riddles:
        return riddles.pop(0)
    else:
        return 'no_riddles_left'


@app.route('/riddle', methods=['GET', 'POST'])
def render_riddle():
    
    return render_template('riddle.html')


 
        



if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),           
            debug=True)

