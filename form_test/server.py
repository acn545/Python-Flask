from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# the index route wil handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this will handle form submissions
# methods=['POST']  defines which methods can be allowed, in this case onlly POST
@app.route('/users', methods=['POST'])
def create_user():
    print "got POST info"
    name = request.form['name']
    email = request.form['email']
    # redirect will take use back to the / original route
    return render_template('success.html')

@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template("user.html")

app.run(debug=True) #runs the server in debug mode

