import sqlite3
import requests
import os
from flask import Flask, request, redirect, session, jsonify
from json import dumps
from flask_cors import CORS, cross_origin
from flask_cas import CAS, login, logout, login_required
from urllib.parse import urlencode
# from cas import CASClient
from databaseConfig import searchEventsDatabase

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'
CORS(app)



app.config['CAS_SERVER'] = 'https://secure.its.yale.edu/cas/'
app.config['CAS_AFTER_LOGIN'] = '/cas_callback'
# app.config['CAS_AFTER_LOGIN'] = 'http://localhost:3000'

cas = CAS(app)

@login_required
@app.route('/')
@app.route('/events/<searchTerm>')
@cross_origin(supports_credentials=True)
def index(searchTerm=""):
    print("hello")


    return dumps(searchEventsDatabase(searchTerm))


if __name__ == '__main__':
    app.run(debug=True)