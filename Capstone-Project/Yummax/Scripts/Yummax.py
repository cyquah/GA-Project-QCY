import numpy as np
import pandas as pd
import pickle
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, session, escape, redirect, url_for, render_template, request

app = Flask(__name__)
# set the secret key
app.secret_key = '\x1d\xfa\xb5s\xf1\x03\x11Z)@\x10\x983B\xec\x88I\xe6\xbe\x19-\xc7\xe4\x86'

@app.route('/')
def welcome():
    return render_template('Yummax_admin.html')

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return welcome()
    else:
        return render_template('login.html')
 
@app.route('/login', methods = ['POST'])
def admin_login():
    if request.form['password'] == 'gadsi978' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return admin()
    else:
        return 'You are not admin !'    

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return input_()

@app.route('/input')
def input_():
    return render_template('Yummax.html')  

@app.route('/foodtrend')
def foodtrend():
    with open('../../LDA&Sentiment_Analysis/topics_str.pkl', 'rb') as f:
        topics_str = pickle.load(f)

    session['topics'] = topics_str

    with open ('../../LDA&Sentiment_Analysis/Topics.pkl', 'rb') as F:
        Topics = pickle.load(F)

    session['Topics'] = Topics

    return render_template('food_trends.html')

@app.route('/topic_submit', methods = ['POST', 'GET'])
def topic_submit():
    if request.method == 'POST':
        topic = request.form['topic_query']  
        topic = topic.title()

    txt = pd.read_pickle('../../Data-Source-FoodBlogs/FoodBlogs/combined_blogs.pickle')
    nl = []
    for item in txt['Summary']:  
        if topic.lower() in item.lower():
            nl.append(item)

    session['topic_ls'] = nl

    return render_template('food_topic.html', topic=topic)

@app.route('/dining_submit', methods = ['POST', 'GET'])
def dining_submit():
    if request.method == 'POST':
        dining = request.form['dining_query']  
        dining = dining.title()

    txt = pd.read_pickle('../../Data-Source-FoodBlogs/FoodBlogs/combined_blogs.pickle')
    sl = []
    for item in txt['Summary']:  
            if dining.lower() in item.lower():
                sl.append(item)

    analyzer = SentimentIntensityAnalyzer()

    sent_threshold = 0.7

    pos = []
    neu = []
    neg = []
    for i in range(len(sl)):
        vs = analyzer.polarity_scores(sl[i])
        
        if vs['compound'] > sent_threshold:
            pos.append(sl[i])
        elif vs['compound'] < -sent_threshold:
            neg.append(sl[i])
        else:
            neu.append(sl[i])

    if sl:
        pos_percent = int(round(float(len(pos)) / float(len(sl)) * 100))
        neg_percent = int(round(float(len(neg)) / float(len(sl)) * 100))
        neu_percent = int(round(float(len(neu)) / float(len(sl)) * 100))
    else:
        pos_percent = 0
        neg_percent = 0
        neu_percent = 0

    session['pos'] = pos
    session['neg'] = neg
    session['neu'] = neu

    return render_template('dining_option.html', dining=dining, pos_percent=pos_percent, neg_percent=neg_percent, neu_percent=neu_percent)

@app.route('/feedback', methods = ['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        fdbk = request.form['feedback_input']  

    with open('feedback.txt','a') as f:
        f.write(fdbk + '\n')

    return render_template('feedback.html')


if __name__ == '__main__':
    app.run(debug = True)
