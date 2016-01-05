# import the Flask class from the flask module
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, g, jsonify
from functools import wraps
import sqlite3

# create the application object
app = Flask(__name__)

# config
app.secret_key = 'my precious'
app.database = 'sample.db'


# use decorators to link the function to a url
@app.route('/')
def home():
    # return a string
    g.db = connect_db()
    cur = g.db.execute('select * from NationalNames LIMIT 5')
    NationalNames = [dict(Id=row[0], Name=row[1], Year=row[2], Gender=row[3], Count = row[4]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', NationalNames=NationalNames)  # render a template

# count number of entries in a database
@app.route('/entrynumber', methods = ['GET'])
def entrynumber():
    # return a string
    g.db = connect_db()
    cur2 = g.db.execute('SELECT Count(*) FROM NationalNames')
    NationalNames = [dict(Id=row[0]) for row in cur2.fetchall()]
    return jsonify({'The total number of entries based on Id count is' : NationalNames})

#json records for dataset
@app.route('/names', methods = ['GET'])
def  babyname():
    # return a string
    g.db = connect_db()
    cur = g.db.execute('select * from NationalNames LIMIT 20') # limit so as to enhance speed
    NationalNames = [dict(Id=row[0], Name=row[1], Year=row[2], Gender=row[3], Count = row[4]) for row in cur.fetchall()]
    #namebaby = [NationalName for NationalName in NationalNames if NationalName ['Name'] == name]
    return jsonify({'Baby names are ' : NationalNames})

#get all entries for a specific baby name
@app.route('/names/<string:name>', methods = ['GET'])
def  returnOne(name):
    # return a string
    g.db = connect_db()
    cur = g.db.execute('select * from NationalNames LIMIT 100') # limit so as to enhance speed
    NationalNames = [dict(Id=row[0], Name=row[1], Year=row[2], Gender=row[3], Count = row[4]) for row in cur.fetchall()]
    namebaby = [NationalName for NationalName in NationalNames if NationalName ['Name'] == name]
    return jsonify({'Baby name detail is' : namebaby[0]})
   

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# connect to database
def connect_db():
    return sqlite3.connect(app.database)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
