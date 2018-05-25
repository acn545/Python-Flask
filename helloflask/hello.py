''' imports flask'''
from flask import Flask, render_template
app = Flask(__name__)
''' @app declares an opperator like we used $ for Jquery in JavaScrip'''
@app.route('/success')
def sucess():
    return render_template('success.html')

@app.route('/')
def hello_world():
    return "hello World"
# this line will activate the server
app.run(debug=True)

