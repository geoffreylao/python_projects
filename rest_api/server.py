import flask
from flask import request, jsonify
import sqlite3
import json

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
    
    result = {"message" : "succcess"}

    result["person"] = request.json
    return(result)

#TODO: add a POST endpoint for adding people 
@app.route('/add', methods=['POST'])
def insert():
    person = request.json

    name = person["name"]
    age = person["age"]
    occupation = person["occupation"]

    params = (name, age, occupation)

    conn = sqlite3.connect('people.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute("INSERT INTO people VALUES (NULL, ?, ?, ?)", params)
    conn.commit()
    result = {"message" : "succcess"}

    result["person"] = request.json
    return(result)

#TODO: add a DELETE endpoint for removing people 
@app.route('/remove', methods=['POST'])
def delete():
    person_id = request.json["id"]
    
    conn = sqlite3.connect('people.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute(f"DELETE FROM people WHERE id = {person_id}")
    conn.commit()

    result = {"message" : "succcess"}

    result["person"] = request.json
    return(result)

#TODO: add a PUT endpoint for updating people 
@app.route('/update', methods=['PUT', 'POST'])
def update():
    query = "UPDATE people SET name = 'wario' WHERE name = 'mario'"

    person_id = request.json["id"]
    name = request.json["name"]

    conn = sqlite3.connect('people.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute(f"UPDATE people SET name = \"{name}\" WHERE id = {person_id}")
    conn.commit()

    result = {"message" : "succcess"}

    result["person"] = request.json
    return(result)

app.run()