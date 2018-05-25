from flask import Flask, flash, render_template, redirect, request, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/sub", methods=['POST'] )
def submission():
    name = request.form['name']
    city = request.form['city']
    lang = request.form['language']
    area = request.form['area']
    if request.method == 'POST':
        if len(request.form['name']) < 1:
            flash("user must have a name")
            print "name validation"
            return redirect('/')
        elif len(request.form['area']) < 1:
            flash("You must add a comment")
            print "comment validation"
            return redirect('/')
        elif len(request.form['area']) > 120:
            flash("comment is to long")
            print " to long vallidation"
            return redirect('/')
        else:
            print "this worked"
        return render_template("submission_form.html", name=name, city = city, lang = lang, area=area)
    else:
        print "DEBUG: save() GET method was called"
   

app.run(debug=True)