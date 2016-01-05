# import the Flask class from the flask module
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, g, jsonify,json
#from functools import wraps
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
    cur = g.db.execute('select * from NationalNames LIMIT 5') # limit so as to enhance speed
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
    return jsonify({'Baby names are ' : NationalNames})

#get all entries for a specific baby name
@app.route('/names/<string:name>', methods = ['GET'])
def  returnOne(name):
    # return a string
    g.db = connect_db()
    cur = g.db.execute('select * from NationalNames LIMIT 100') # limit so as to enhance speed
    NationalNames = [dict(Id=row[0], Name=row[1], Year=row[2], Gender=row[3], Count = row[4]) for row in cur.fetchall()]
    namebaby = [NationalName for NationalName in NationalNames if NationalName ['Name'] == name]
    return jsonify({'Baby name details are' : namebaby[0]})

# list of all unique baby names
@app.route('/unique', methods = ['GET'])
def unique():
    # return a string
    g.db = connect_db()
    cur2 = g.db.execute('select * from NationalNames group by Name LIMIT 10')
    #cur = g.db.execute('select avg(Count) from NationalNames LIMIT 10')
    NationalNames = [dict(Name=row[1], Year=row[2], Count = row[4]) for row in cur2.fetchall()]
    #NationalNames2 = [dict(Count = row[2]) for row in cur.fetchall()]
    return jsonify({'Unique names are' : NationalNames})

#add entry to database 
@app.route('/add', methods=['POST'])
def add_entry():
    cur = g.db.cursor()
    g.db.execute('insert into NationalNames (Gender, Year, Count) values (?, ?, ?)',
                 [request.json['gender'], request.json['year'], request.json['count']])
    g.db.commit()
    id = cur.lastrowid
    cur.close()
    flash('New entry was successfully posted')
    return "id"


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# connect to database
def connect_db():
    return sqlite3.connect(app.database)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
