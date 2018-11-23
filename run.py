from flask import Flask

app = Flask(__name__)

usernames = []
riddles = {} # including answers
user_answers = {}