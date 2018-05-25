from flask import Flask, flash, render_template, redirect, request, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST', 'GET'])
def process():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    cpassword = request.form['cpassword']
    if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1 or len(password) < 1 or len(cpassword) < 1:
        flash("Feild Missing, please fillout every box")
        print "something smissing"
    elif not EMAIL_REGEX.match(email):
        flash("invalid email address")
        print "email bad"
    elif len(password) > 8:
        flash("password should be no longer than 8 characters")
    elif password != cpassword:
        flash("Passwords do not match")
    elif first_name.isalpha() != True or last_name.isalpha() != True:
        flash('invalid name')
    else:
        flash("thank you for submitting your information")
        
    return redirect('/')




app.run(debug=True)