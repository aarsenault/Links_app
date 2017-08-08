from flask import render_template, request, session, url_for
from werkzeug.utils import redirect
from app.models.users import User
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.is_login_valid(email, password):
            session['email'] = email
            return redirect(url_for('profile'))
    return redirect(url_for('index'))

@app.route('/logout', methods=['GET'])
def logout():
    session['email'] = None
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    user = {'name': 'Nasreen'}  # fake user
    links = [  # fake array of posts
        {
            'author': 'users',
            'date' : "04-08-2017",
            'description': 'cool information site',
            'link': 'https://www.wikipedia.org',
            'tags': None
        },
        {
            'author': 'user',
            'date' : "06-08-2017",
            'description': 'worst site I\'ve ever used',
            'link': 'www.facebook.org',
            'tags': None
        },
        {
            'author': 'user',
            'date' : "01-08-2017",
            'description': 'other cool site',
            'link': 'www.python.org',
            'tags': None
        }
    ]

    return render_template("profile.html",
                           user=user['name'],
                           links=links)
