from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/display')
def display():
    return render_template("dojos.html")

@app.route('/dojo/new', methods=['GET', 'POST'])
def dojo_new():
    name = request.form['name']
    email = request.form['email']
    return render_template("new.html")
app.run(debug=True)