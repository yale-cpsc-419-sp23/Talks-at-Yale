import sqlite3
import os
from flask import Flask, request, redirect, session, jsonify
from json import dumps
from flask_cors import CORS
from flask_cas import CAS, login, logout, login_required
from urllib.parse import urlencode

# from cas import CASClient

from databaseConfig import searchEventsDatabase

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'
CORS(app)



app.config['CAS_SERVER'] = 'https://secure.its.yale.edu/cas/'
app.config['CAS_AFTER_LOGIN'] = 'cas_callback'
# app.config['CAS_AFTER_LOGIN'] = 'http://localhost:3000'

cas = CAS(app)

@app.route('/')
@app.route('/events/<searchTerm>')
def index(searchTerm=""):
    """returns a list of events that match the search term"""
    print("hello")
    print("USERNAME")
    print(cas.username)
    if not cas.username:
        protected_resource_url = request.url
        # service_url = request.url
        # cas_login_url = cas.get_login_url(service=service_url)
        next_url = 'http://127.0.0.1:5000/cas_callback'
        new_url = app.config['CAS_SERVER'] + "login?" + urlencode({'service': 'http://localhost:3000/'})
        print(new_url)
        return jsonify({'login_url': new_url})
        # return [new_url]
    #     # return jsonify({'success': False, 'data': new_url})
    #     # return jsonify({'success': True, 'result': dumps(searchEventsDatabase(searchTerm))})

    

    print("User is authenticated:", cas.username)
    # if not cas.username:
    #     cas.login()
    print(cas.attributes)
    # return jsonify({'success': True, 'result': dumps(searchEventsDatabase(searchTerm))})
    # return dumps(searchEventsDatabase(searchTerm))
    return jsonify({'results': dumps(searchEventsDatabase(searchTerm))})


# @app.route('/login')
# def login():
#     cas.login

@app.route('/cas_callback')
def cas_callback():
  print("reached cas_callback")
  
  # redirect the user back to the homepage
  redirect_url = 'http://localhost:3000/'
  return jsonify({'redirect_url': redirect_url})


if __name__ == '__main__':
    app.run(debug=True)