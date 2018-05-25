from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ninja")
def ninjas():
    name = "tmnt.png"
    print name
    return render_template('index.html', nam = name)

@app.route("/ninja/<name>")
def turtle(name):
    name = name + ".jpg"
    print name
    return render_template('index.html', nam = name)


app.run(debug=True)

