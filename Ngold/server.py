from flask import Flask, session, render_template, redirect, request
from random import randrange
app = Flask(__name__)
app.secret_key= "key"
coins = 0
ncoins = 0
listitems = []
@app.route('/', methods=['GET', 'POST'])
def index():
    print coins
    return render_template('index.html', coins = coins, ncoins = ncoins)

@app.route('/process_money', methods=['GET', 'POST'])
def money():
    if request.method == 'POST':
        if request.form['nam'] == 'farm':
            global coins
            print "farm request"
            ncoins = randrange(10, 20)
            coins += session['ncoins']
            listitems.append('At the farm you collected ' + str(ncoins) + ' coins! ')
            session['append'] = listitems
            return redirect('/')
        elif request.form['nam'] == 'cave':
            ncoins = randrange(5,10)
            coins += ncoins
            print 'cave'
            listitems.append('At the cave you collected ' + str(ncoins) + ' coins! ')
            session['append'] = listitems
            return redirect('/')
        elif request.form['nam'] == 'house':
            ncoins = randrange(2, 5)
            coins += ncoins
            print 'house'
            listitems.append('At the house you collected '+ str(ncoins) + ' coins! ')
            session['append'] = listitems
            return redirect('/')
        elif request.form['nam'] == 'casino':
            ncoins = randrange(-50, 50)
            coins += ncoins
            print 'casino'
            listitems.append('At the casino you collected '+ str(ncoins) + ' coins! ')
            session['append'] = listitems
            return redirect('/')
    else:
        "DEBUG: save() GET method was called"
app.run(debug=True)

