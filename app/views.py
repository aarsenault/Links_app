from flask import render_template
from app import app


@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/profile')



def profile():
    user = {'name': 'Nasreen'}  # fake user
    links = [  # fake array of posts
        {
            'author': user,
            'date' : "04-08-2017",
            'description': 'cool information site',
            'link': 'https://www.wikipedia.org',
            'tags': None
        },

        {
            'author': user,
            'date' : "06-08-2017",
            'description': 'worst site I\'ve ever used',
            'link': 'www.facebook.org',
            'tags': None
        },

        {
            'author': user,
            'date' : "01-08-2017",
            'description': 'other cool site',
            'link': 'www.python.org',
            'tags': None
        }

    ]
    return render_template("profile.html",
                           user=user,
                           links=links)
