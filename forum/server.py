from flask import Flask, redirect, request, session, flash, render_template
from mysqlconnection import MySQLConnector
import re
import md5

app = Flask(__name__)
app.secret_key="some key thats secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'forums')

@app.route('/')
def input():
    if "email" in session:
       return redirect('/dashboard')
    else:
        return render_template('index.html')
    
@app.route('/login', methods=['POST'])
def long():
    form = request.form
    session['email'] = form['email']
    if form['email'] < 0 or not EMAIL_REGEX.match(form['email']):
        flash('Please enter a valid Email address')
        return redirect('/')
    elif form['password'] < 1:
        flash("Please enter a password")
        return redirect('/')
    else:
        hashed_password = md5.new(form['password']).hexdigest()
        session['password'] = hashed_password
        query = "SELECT * FROM users WHERE email = :email and password = :password"
        data = {
            "email": form['email'],
            "password": hashed_password
        }
        users = mysql.query_db(query,data)
        if len(users) > 0:
            user = users[0]
            if hashed_password == user['password'] and session['email'] == user['email']:
                return redirect('/dashboard')
    flash('Log in FAILED try again')
    return redirect('/')

@app.route('/register',  methods=['GET','POST'])
def register():
    return render_template('registration_form.html')

@app.route('/registration',  methods=['GET','POST'])
def registration():
    form = request.form 
    if len(form['first_name']) < 1 or len(form['last_name']) < 1:
        flash("Please Enter a valid name")
    elif len(form['email']) < 1 or not EMAIL_REGEX.match(form['email']):
        flash("Please Enter a valid email address")
    elif len(form['password']) < 1 or form['password'] != form['cpassword']:
        flash("password is invalid or does not match")
    else:
        session['email'] = form['email']
        hashed_password = md5.new(form['password']).hexdigest()
        query = "INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW());"
        data ={
            'first_name': form['first_name'],
            'last_name': form['last_name'],
            'email': form['email'],
            'password': hashed_password
        }
        mysql.query_db(query,data)
        return redirect('/dashboard')
    return redirect('/register')

@app.route('/dashboard')
def dash():
    
    query = "SELECT  email, password, messages.user_id, messages.message, messages.created_at, messages.updated_at, messages.id, first_name, last_name FROM users JOIN messages ON messages.user_id = users.id"
    messages = mysql.query_db(query)
    queryM = "SELECT  * FROM users JOIN messages ON messages.user_id = users.id JOIN comments ON comments.userid = users.id"
    comments = mysql.query_db(queryM)
    return render_template('dashboard.html', messages = messages, comments = comments)

@app.route('/post_message', methods=['POST'])
def post():
    form = request.form
    query = "SELECT * FROM users WHERE email = :email"
    data = {
        "email": session['email'],
    }
    users = mysql.query_db(query,data)
    user = users[0]
    queryM = "INSERT INTO `messages` (`message`, `created_at`, `updated_at`, `user_id`) VALUES (:message, NOW(), NOW(), :user_id);"
    dataM ={
        'message': form['message'],
        'user_id': user['id']
    }
    mysql.query_db(queryM, dataM)
    return redirect('/dashboard')

@app.route('/post_comment', methods=['POST'])
def comment():
    form = request.form
    query = "SELECT * FROM users WHERE email = :email"
    data = {
        "email": session['email'],
    }
    users = mysql.query_db(query,data)
    user = users[0]
    queryC = "INSERT INTO `comments` (`comment`, `created_at`, `updated_at`, `userid`, `message_id`) VALUES (:comment, NOW(), NOW(), :user_id, :message_id);"
    dataC ={
        'comment': form['comment'],
        'user_id': user['id'],
        'message_id': request.form['msg_id']
    }
    mysql.query_db(queryC, dataC)
    return redirect('/dashboard')


app.run(debug=True)