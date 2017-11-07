import numpy as np
import pandas as pd
import pickle

from flask import Flask, session, escape, redirect, url_for, render_template, request

app = Flask(__name__)
# set the secret key
app.secret_key = '\x1d\xfa\xb5s\xf1\x03\x11Z)@\x10\x983B\xec\x88I\xe6\xbe\x19-\xc7\xe4\x86'

@app.route('/')
def admin():
    return render_template('Yummax_admin.html')

@app.route('/input')
def input():
    return render_template('Yummax.html')  

@app.route('/foodtrend')
def foodtrend():
    with open('topics_str.pkl', 'rb') as f:
        topics_str = pickle.load(f)

    session['topics'] = topics_str

    with open ('Topics.pkl', 'rb') as F:
        Topics = pickle.load(F)

    session['Topics'] = Topics

    return render_template('food_trends.html')

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        result = request.form  # dictionary
        x = result.keys()  # x[0] is duration and x[1] is amount
        y = result.values()
        with open('input.csv', 'w') as sm:
            smwriter = csv.writer(sm, delimiter=' ')
            smwriter.writerow(y)
    return redirect(url_for('search'))

if __name__ == '__main__':
    app.run(debug = True)
