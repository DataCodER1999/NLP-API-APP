from flask import Flask,render_template,request,redirect
from db import Database
import api
dbo = Database()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def registration():
    return render_template('registration.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    ans = dbo.register(name,email,password)

    if ans:
        return  render_template('login.html',message='Registration successfull | Login Now')

    else:
        return render_template('registration.html',message='Email already exists')

@app.route('/perform_login',methods=['post'])
def login_operation():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    ans = dbo.login_check(email,password)

    if ans:
        return  redirect('/profile')
    else:
        return render_template('login.html',message='Incorrect email/password')

@app.route('/ner')
def ner():
    return render_template('ner.html')


@app.route('/perform_ner',methods=['post'])
def perform_ner():

        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)

        return render_template('ner.html', response=response)


@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template('sentiment_analysis.html')

@app.route('/perform_sentiment_analysis',methods=['post'])
def perform_sentiment_analysis():
    text = request.form.get('sentiment_text')
    response = api.sentiment_analysis(text)

    return  render_template('sentiment_analysis.html',response=response)


@app.route('/profile')
def profile():
    return  render_template('profile.html')

app.run(debug=False,host='0.0.0.0')