"""
The api routes of the uses such as login, logout will be included in this file
"""
from app.users import bp_users
from flask import request, jsonify, redirect, url_for, make_response
from app import app, db
from app.models import User
from urllib.parse import urlencode
import requests
from xml.etree import ElementTree
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import yalies

###--------------Logging Users In --------------####
###---------------------------------------------####
@bp_users.route('/login', methods=['GET'])
@jwt_required(optional=True)
def login():
    """Handles login using Yale's CAS"""
    identity = get_jwt_identity()
    if identity:
        print("In session.")
        frontend_url = 'http://localhost:3000'
        return redirect(frontend_url)

    # url to be directed to when a user logs in using yale's cas
    service_url = url_for('users.after_login', _external=True)
    cas_login_url = app.config['CAS_SERVER'] + app.config['CAS_LOGIN_ROUTE'] + '?' + urlencode({'service': service_url})
    return redirect(cas_login_url)

@bp_users.route('/cas-callback', methods=['GET'])
def after_login():
    """A function that validates the ticket sent by Yale CAS and gets netid of the user"""

    # the ticket Sent by CAS
    ticket = request.args.get('ticket')
    print("CAS Ticket:", ticket)
    # Validate the ticket with the CAS server
    service_url = url_for('users.after_login', _external=True)
    cas_service_validate_url = f"{app.config['CAS_SERVER']}/serviceValidate?service={service_url}&ticket={ticket}"
    response = requests.get(cas_service_validate_url)

    # Parse the XML response
    xml_tree = ElementTree.fromstring(response.content)
    username_tag = xml_tree.find('.//{http://www.yale.edu/tp/cas}user')

    if username_tag is not None:
        username = username_tag.text.strip()
        print("Extracted Username:", username)
    else:
        print("Username not found in the response")

    net_id = username

    # Check if a user is already in the database
    user = User.query.filter_by(netid=net_id).first()

    # If not, create a new user
    if not user:
        person = get_user(net_id)
        user = User(netid=person.netid, email=person.email, first_name=person.first_name, last_name=person.last_name, year=person.year, college=person.college, birthday=person.birthday)
        db.session.add(user)
        db.session.commit()
    # Create JWT access token
    access_token = create_access_token(identity=net_id)
    print(access_token)
    is_production = app.config.get('PRODUCTION', False)
    # Send cookie to the front end
    frontend_url = 'http://localhost:3000'
    resp = make_response(redirect(frontend_url))
    resp.set_cookie('access_token', access_token, secure=is_production)
    return resp

@bp_users.route('/is_logged_in', methods=['GET'])
@jwt_required(optional=True)
def is_logged_in():
    """A function that Checks if a user is logged in"""
    token = request.headers.get('Authorization')
    print("Received token:", token)
    identity = get_jwt_identity()
    print("Identity:", identity)
    if identity:
        print("In session")
        return jsonify({'logged_in': True, 'username': identity})
    else:
        print("Logged in is false")
        return jsonify({'logged_in': False}), 200

@bp_users.route('/logout', methods=['GET'])
def logout():
    """A function that Logs out the user from the system"""
    print("In logout.")
    # clear JWT token cookie
    response = make_response(jsonify({"cas_logout_url": app.config['CAS_SERVER'] + app.config['CAS_LOGOUT_ROUTE']}))
    response.delete_cookie('access_token')
    return response




####----Helper Functions----##
def get_user(netid):
    """Getting user information from yalies.io"""
    token = app.config['API_TOKEN']
    api = yalies.API(token)

    person = api.person(filters={'netid': netid})
    print(person.raw)
    return person