from flask import Flask, session , render_template, redirect, request
from random import *
app = Flask(__name__)
app.secret_key = "key"

@app.route('/', methods=['POST', 'GET'])
def index():
    session['number'] = randrange(0, 101)
    print session['number']
    show = "visibility: hidden"
    return render_template('index.html', show = show)

@app.route('/guess', methods=['POST'])
def guess():
    if request.method == 'POST':
        session['guess'] = request.form['guess']
        if int(session['guess']) > int(session['number']):
            print session['guess']
            print session['number']
            color = "background-color: red"
            show = "visibility: show"
            words = "incorrect!! TO HIGH"
            showw = "visibility: hidden"
            return render_template('index.html', guess = session['guess'], show = show, color=color, words=words, showw=showw)
        if int(session['guess']) < int(session['number']):
            print session['guess']
            print session['number']
            color = "background-color: red"
            show = "visibility: show"
            words = "incorrect!! TO LOW"
            showw = "visibility: hidden"
            return render_template('index.html', guess = session['guess'], show = show, color=color, words=words, showw=showw)
        else:
            print session['guess']
            print session['number']
            color = "background-color: green"
            show = "visibility: show"
            words = "correct!!!"
            showw = "visibility: show"
            return render_template('index.html', guess = session['guess'], show = show, color=color, words=words, showw =  showw)
    else:
        "DEBUG: save() GET method was called"

app.run(debug=True)