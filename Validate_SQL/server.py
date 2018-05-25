from flask import Flask, session, render_template,request, flash, redirect
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'validate')
app.secret_key = "key"

@app.route('/')
def index():
    query = 'SELECT * FROM emails'
    emails = mysql.query_db(query)
    return render_template('index.html', emails = emails)

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if len(request.form['email'] ) < 1 or not EMAIL_REGEX.match(request.form['email'] ):
        flash('Email is not in the correct from, please try again')
        print "email is not correct"
        return redirect('/')
    else:
        print "the query is attempting to run"
        query = "INSERT INTO emails(email,  created_at, updated_at) VALUES (:emails, NOW(), NOW())"
        data = {
        'emails': request.form['email'],
     
        }
        mysql.query_db(query,data)
        return redirect('/success')
  
@app.route('/success')
def success():
    flash('Email added successfully')
    query = 'SELECT * FROM emails'
    emails = mysql.query_db(query)
    return render_template('success.html', emails = emails)
@app.route('/delete', methods=['GET', 'POST'])
def delte():
    flash('Email deleted successfully')
    query = "DELETE FROM emails WHERE email = :delete"
    data = {
        "delete": request.form['delete']
    }
    mysql.query_db(query,data)
    return redirect('success')


app.run(debug=True)
    
