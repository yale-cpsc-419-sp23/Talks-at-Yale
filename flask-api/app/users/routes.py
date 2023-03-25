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
@jwt_required(optional=True)
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
    user = User.query.filter_by(username=net_id).first()

    # If not, create a new user
    if not user:
        user = User(username=net_id)
        db.session.add(user)
        db.session.commit()

    # add user to session
    user = User.query.filter_by(username=net_id).first()
    # Create JWT access token
    access_token = create_access_token(identity=net_id)
    print(access_token)
    # Send cookie to the front end
    frontend_url = 'http://localhost:3000'
    resp = make_response(redirect(frontend_url))
    resp.set_cookie('access_token', access_token, secure=False)
    return resp

@bp_users.route('/is_logged_in', methods=['GET'])
@jwt_required(optional=True)
def is_logged_in():
    """A function that Checks if a user is logged in"""
    identity = get_jwt_identity()
    print(identity)
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
    response = make_response(redirect(url_for('users.cas_logout')))
    response.set_cookie('access_token', '', expires=0)
    # Include the CAS logout URL in the response
    cas_logout_url = app.config['CAS_SERVER'] + app.config['CAS_LOGOUT_ROUTE']
    return jsonify(logged_in=False, cas_logout_url=cas_logout_url)

@bp_users.route('/cas_logout', methods=['GET'])
def cas_logout():
    # Redirect the user to the CAS logout page
    cas_logout_url = app.config['CAS_SERVER'] + app.config['CAS_LOGOUT_ROUTE']
    return redirect(cas_logout_url)