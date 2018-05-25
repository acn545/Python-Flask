from flask import Flask, session, flash, render_template, redirect, request
import md5, re
from mysqlconncection import MySQLConnector
app = Flask(__name__)
app.secret_key="keyis a secret"
mysql = MySQLConnector(app, "friendsdb")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    query = "SELECT * FROM friends"
    friendsdb = mysql.query_db(query)
    return render_template('index.html', friendsdb = friendsdb)

@app.route('/users/new')
def new(): 
    return render_template('adduser.html')
@app.route('/users/news', methods=['POST'])
def news():
    form = request.form 
    if len(form['first_name']) <  1 or len(form['last_name']) < 1:
        flash("enter a valid name")
        return redirect('/users/new')
    elif len(form['email']) < 1 or not EMAIL_REGEX.match(form['email'] ):
        flash('please enter a valid email address')
        return redirect('users/new')
    query = "INSERT INTO `friends` (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES (:first_name, :last_name, :email, NOW(), NOW());"
    data = {
        "first_name": form['first_name'],
        "last_name": form['last_name'],
        "email": form['email']
    }
    mysql.query_db(query, data)
    return redirect('/users/new')

@app.route('/users/<id>')
def show(id):  
    ids = id.replace(">", "")
    ids = ids.replace("<", "")
    ids = int(ids)
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('show.html', friends = friends, ids = ids)
    
@app.route('/users/<id>/edit')
def edit(id):
    ids = id.replace(">", "")
    ids = ids.replace("<", "")
    ids = int(ids)
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('edituser.html', friends = friends, ids = ids)

@app.route('/users/<id>/edits', methods=['POST'])
def edits(id):
    ids = id.replace(">", "")
    ids = ids.replace("<", "")
    ids = int(ids)
    form = request.form 
    if len(form['first_name']) <  1 or len(form['last_name']) < 1:
        flash("enter a valid name")
        return redirect('/users')
    elif len(form['email']) < 1 or not EMAIL_REGEX.match(form['email'] ):
        flash('please enter a valid email address')
        return redirect('/users')
    query ="UPDATE `friends` SET `first_name`= :first_name, `last_name`= :last_name, `email`= :email, `updated_at` = NOW() WHERE `id`= :ids;"
    data = {
        'first_name': form['first_name'],
        'last_name': form['last_name'],
        'email': form['email'],
        'ids': ids
    }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/users/<id>/destroy')
def delete(id):
    ids = id.replace(">", "")
    ids = ids.replace("<", "")
    ids = int(ids)
    query = "DELETE FROM `friends` WHERE `id`=:id; "
    data = {
        'id': ids
    }
    mysql.query_db(query, data)
    return redirect('/users')
app.run(debug=True)
