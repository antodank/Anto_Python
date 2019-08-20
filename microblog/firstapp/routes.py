from firstapp import app
from datetime import datetime
import re
from flask import render_template

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/index/myname")
def printname():
    return "Hello, Ankit"

@app.route("/home")
def showhome():
    user = {'username': 'Ankit'}
    return render_template('home.html', title='Home', user=user)

@app.route("/about")
def showabout():
    return render_template('about.html')

@app.route('/index')
def MainPage():
    return render_template('layout.html', title='First Flask App')

@app.route("/home/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content