# import the Flask class from the flask module
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, g
#from functools import wraps
import sqlite3

# create the application object
app = Flask(__name__)

# config
app.secret_key = 'my precious'
app.database = 'sample.db'


# use decorators to link the function to a url
@app.route('/')
#@login_required
def home():
    # return "Hello, World!"  # return a string
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(Id=row[0], Name=row[1], Year=row[1], Gender=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=posts)  # render a template


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# connect to database
def connect_db():
    return sqlite3.connect(app.database)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
