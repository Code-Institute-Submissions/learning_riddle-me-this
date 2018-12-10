from flask import Flask
import json
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import os

app = Flask(__name__)

usernames = []
user_answers = {}
riddles = ''


def read_riddlesjson():
    with open('./data/riddles.json', 'r', encoding='utf-8') as f:
        riddles = json.loads(f.read())
    return riddles
riddles = read_riddlesjson()


def next_riddle(riddles):
    if riddles:
        riddle = riddles.pop(0)
        del riddles[0]
    return riddle


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


# @app.route('/<username>')
# def user(username):
#     return username


@app.route('/print_users')
def print_users():
    all_users = ''
    for user in usernames:
        all_users += user + ' '
    return all_users


@app.route('/<username>', methods=['GET', 'POST'])
def render_riddle(username):
    print('\n\nBefore LOCALS render_riddle', sorted(locals().keys()))
    riddle = next_riddle(riddles)
    if riddle:
        print('\n\n LOCALS render_riddle', sorted(locals().keys()))
        return render_template('riddle.html', riddle=riddle['riddle'])
    else:
        riddle = 'End'
        return riddle


if __name__ == '__main__':
    print('\n\n CALLING FUNCTION app.run\n\n')
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),           
            debug=True)

