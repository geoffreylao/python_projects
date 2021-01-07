import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
'''
    This is a very simple REST API to satify basic CRUD requirements on a sqlite db
'''

# Helper fucntion for converting results to dictionary from sqlite 
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Default endpoint, this is what gets executed when you go to the default page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Super Simple API</h1>
              <p>Pretty useless atm</p>'''


#Simple get all 
# TODO: Add parameter to select certain people based on id, name, age, etc
@app.route('/people', methods=['GET'])
def people():
    query = "SELECT * FROM people"

    conn = sqlite3.connect('people.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query).fetchall()
    return jsonify(results)

#TODO: add a POST endpoint for adding people 
@app.route('/add', methods=['GET', 'POST'])
def insert():
    query = "INSERT INTO people VALUES ( 1, 'luigi', 69, 'jumper')"

    conn = sqlite3.connect('people.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute(query)
    conn.commit()

    query = "SELECT * FROM people"
    results = cur.execute(query).fetchall()
    return jsonify(results)

#TODO: add a DELETE endpoint for removing people 
@app.route('/remove', methods=['GET', 'POST'])
def delete():
    query = "DELETE FROM people WHERE id = 1"

    conn = sqlite3.connect('people.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute(query)
    conn.commit()

    query = "SELECT * FROM people"
    results = cur.execute(query).fetchall()
    return jsonify(results)

#TODO: add a PUT endpoint for updating people 
@app.route('/update', methods=['PUT', 'GET', 'POST'])
def update():
    query = "UPDATE people SET name = 'wario' WHERE name = 'mario'"

    conn = sqlite3.connect('people.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute(query)
    conn.commit()

    query = "SELECT * FROM people"
    results = cur.execute(query).fetchall()
    return jsonify(results)


@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        username = request.form['username']
    return "test page"

app.run()