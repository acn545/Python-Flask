from flask import Flask, render_template, session, request, redirect
app =Flask(__name__)
app.secret_key = "key"
@app.route('/')
def index():
    session['i'] = 0
    return redirect('/i')

@app.route('/i')
def index1():
    session['i'] = session['i'] + 1
    return render_template("index.html")

@app.route('/by2')
def by2():
    session['i'] += 1
    return redirect('/i')
@app.route('/reset')
def rest():
    return redirect('/')

app.run(debug=True)