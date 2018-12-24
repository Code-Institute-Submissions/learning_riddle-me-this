from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'some_secret'

usernames = []
user_answers = {}
riddles = []
answered_riddles = []
riddle_id = '1'


def read_riddlesjson():
    with open('./data/riddles.json', 'r', encoding='utf-8') as f:
        riddles = json.load(f)
    return riddles
riddles = read_riddlesjson()
print('after getting info from JSON file', riddles['1'])



# def get_riddle():
#     print('get_riddle', riddle)
#     return riddle, riddle['riddle_id']


# def next_riddle():
#     print('getting next riddle')
#     if riddles:
#         riddle = riddles.pop(0)
#     print('inside next_riddle', riddle)
#     return riddle, riddle['riddle_id']


def check_is_correct(usr_answer, riddle_id):
    print('check_is_correct', riddle_id)
    right_answer = riddles[riddle_id]['answer'].lower()
    is_correct = (True if usr_answer == right_answer else False)
    return is_correct
    

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
        return redirect(url_for('render_riddle',   #  url_for ???
                                username=username, riddle_id=riddle_id))
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


@app.route('/riddle/<username>/<riddle_id>', methods=['GET', 'POST'])
def render_riddle(username, riddle_id):
    """
    Display a riddle and a text box to answer it.
    """
    
    #riddle, riddle_id = get_riddle()
    print('start render_riddle', riddle_id)
    
    if request.method == 'POST':
        usr_answer = request.form['answer'].lower()
        is_correct = check_is_correct(usr_answer, riddle_id)
    
        if not is_correct:
            print('not correct render_riddle', riddle_id)
            flash('The answer is not correct, try again!')
            return render_template('riddle.html', 
                                    riddle_text=riddles[riddle_id]['question'])
        if is_correct:
            print('start correct render_riddle', riddle_id)
            #riddle, riddle_id = next_riddle()
            #print('after calling next_riddle', riddle)
            riddle_id = str(int(riddle_id) + 1)
            return redirect(url_for('render_riddle', 
                                    username=username, 
                                    riddle_id=riddle_id))
    print('before last return function in render_riddle', riddle_id)
    return render_template('riddle.html', 
                            riddle_text=riddles[riddle_id]['question'])


if __name__ == '__main__':
    print('\n\n CALLING FUNCTION app.run\n\n')
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', '8080')),           
            debug=True)

