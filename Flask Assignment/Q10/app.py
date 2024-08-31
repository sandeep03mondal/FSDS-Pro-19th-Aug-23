# Design a Flask app with proper error handling for 404 and 500 errors

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Home Page'

@app.route('/cause_404')
def cause_404():
    #
