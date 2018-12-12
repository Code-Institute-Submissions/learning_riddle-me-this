from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import json
import os

app = Flask(__name__)

usernames = []
user_answers = {}
riddles = []
answered_riddles = []


def read_riddlesjson():
    with open('./data/riddles.json', 'r', encoding='utf-8') as f:
        riddles = json.load(f)
    return riddles
riddles = read_riddlesjson()


def next_riddle(riddles):
    if riddles:
        riddle = riddles.pop(0)
    return riddle, riddle['riddle_id']


def store_answered_riddles(riddle_id, answer):
    answered_riddles.append({'riddle_id': riddle_id, 'answer': answer})
    return answered_riddles


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Landing page with form to submit username
    """
    if request.method == 'POST':
        username = request.form['username']
        if username not in usernames:
            usernames.append(username)
            print('\n', username, '\n')
        return redirect(url_for('render_riddle', 
                                username=username))
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


@app.route('/riddle/<username>', methods=['GET', 'POST'])
def render_riddle(username):
    """
    Display a riddle and a text box to answer it.
    """
    riddle_text = riddles[1]['riddle']
    
    if request.method == 'POST':
        answer = request.form['answer'].lower()
        right_answer = riddles[1]['answer'].lower()
        is_correct = (True if answer == right_answer else False)
        return (str(is_correct) , answer)
        
    return render_template('riddle.html', riddle_text=riddle_text)


if __name__ == '__main__':
    print('\n\n CALLING FUNCTION app.run\n\n')
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),           
            debug=True)

