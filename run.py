from collections import OrderedDict
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
riddles = []
scores = {}
points_right_ans = 5
points_wrong_ans = -1
riddle_id = '1'


def read_riddlesjson():
    with open('./data/riddles.json', 'r', encoding='utf-8') as f:
        riddles = json.load(f)
    return riddles
riddles = read_riddlesjson()


def check_is_correct(usr_answer, riddle_id):
    print('check_is_correct', riddle_id)
    right_answer = riddles[riddle_id]['answer'].lower()
    is_correct = (True if usr_answer == right_answer else False)
    return is_correct
    

def update_scores(user, score):
    if scores.get(user, 'no_usr') == 'no_usr': scores[user] = 0 
    scores[user] = scores[user] + score
    return scores


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
                                username=username, 
                                riddle_id=riddle_id))
    return render_template('index.html')


# For testing purposes
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
    print('start render_riddle', riddle_id)
    
    if int(riddle_id) > len(riddles): 
        return redirect(url_for('render_leaderboard'))
    
    if request.method == 'POST':
        usr_answer = request.form['answer'].lower()
        is_correct = check_is_correct(usr_answer, riddle_id)
    
        if not is_correct:
            scores = update_scores(username, points_wrong_ans)
            print('not correct render_riddle', riddle_id, scores)
            flash('The answer is not correct, try again!')
            return render_template('riddle.html', 
                                    riddle_text=riddles[riddle_id]['question'])
        if is_correct:
            scores = update_scores(username, points_right_ans)
            print('start correct render_riddle', riddle_id, scores)
            riddle_id = str(int(riddle_id) + 1)
            return redirect(url_for('render_riddle', 
                                    username=username, 
                                    riddle_id=riddle_id))
    print('before last return function in render_riddle', riddle_id)
    return render_template('riddle.html', 
                            riddle_text=riddles[riddle_id]['question'])


@app.route('/leaderboard')
def render_leaderboard():
    sorted_scores = OrderedDict(sorted(scores.items(), 
                                       key=lambda t: t[1], 
                                       reverse=True))
    return render_template('leaderboard.html', scores=sorted_scores)


if __name__ == '__main__':
    print('\n\n CALLING FUNCTION app.run\n\n')
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', '8080')),           
            debug=True)

