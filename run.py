from flask import Flask
import os

app = Flask(__name__)

usernames = []
riddles = {} # including answers
user_answers = {}


@app.route('/')
def index():
    """
    Hello Flask!
    """
    return 'Hello flask!'







if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),           
            debug=True)