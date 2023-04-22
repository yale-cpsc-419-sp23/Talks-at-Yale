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
@bp_users.route('/login/', methods=['GET'])
@jwt_required(optional=True)
def login():
    print("GURJFJEOIRJFJERIOJo")
    """Handles login using Yale's CAS"""
    identity = get_jwt_identity()
    if identity:
        print("In session.")
        frontend_url = 'http://localhost:3000'
        return redirect(frontend_url)

    # url to be directed to when a user logs in using yale's cas
    service_url = url_for('users.after_login', _external=True)
    cas_login_url = "https://secure.its.yale.edu/cas/login" + '?' + urlencode({'service': service_url})
    print(cas_login_url)
    # cas_login_url = app.config['CAS_SERVER'] + app.config['CAS_LOGIN_ROUTE'] + '?' + urlencode({'service': service_url})
    print("LOGGIN IN")
    print(app.config['CAS_SERVER'])
    print(app.config['CAS_LOGIN_ROUTE'])
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
    get_user(net_id)

     # Check if a user is already in the database
    user = User.query.filter_by(netid=net_id).first()

    # Adding profile photo and major
    if user:
        if user.photo_link is None or user.major is None:
            person = get_user(net_id)
            user.photo_link = person.image
            user.major = person.major
            db.session.commit()
    # If not, create a new user
    if not user:
        person = get_user(net_id)
        user = User(netid=person.netid, email=person.email, first_name=person.first_name, last_name=person.last_name, year=person.year, college=person.college, birthday=person.birthday, major=person.major, photo_link=person.image)
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
    homepage = 'http://localhost:3000'
    response = make_response(jsonify({"cas_logout_url": homepage}))
    response.delete_cookie('access_token')
    return response

@bp_users.route('/profile', methods=['GET'])
@jwt_required(optional=True)
def profile():
    """Getting the profile of a user"""
    net_id = get_jwt_identity()
    print(net_id)
    user = User.query.filter_by(netid=net_id).first()

    # get profile details
    profile_json = user.profile()
    print(profile_json)
    return jsonify(profile_json)

@bp_users.route('/remove_friend', methods=['GET','POST'])
@jwt_required(optional=True)
def remove_friend():
    """User removes a friend from their friend list"""

    net_id = get_jwt_identity()
    friend_id = request.args.get('id', '')

    # get user via their net id
    user = User.query.filter_by(netid=net_id).first()
    # get user to remove as friend via their netid
    removed_friend = User.query.filter_by(net_id=friend_id).first()

    # both users should be found. If not there's an error
    if not user or not removed_friend:
        return jsonify({"error": "User not found"}), 404

    # User can only remove friends from their friend list
    if removed_friend not in user.friends:
        return jsonify({"message": "You are not friends with this user"}), 404

    # remove friend from user's friend list
    if removed_friend in user.friends:
        user.friends.remove(removed_friend)
    # remove user from friend's friend list
    if user in removed_friend.friends:
        removed_friend.friends.remove(user)
    db.session.commit()

    return jsonify({"message": "Friend removed"}), 200

@bp_users.route('/add_friend', methods=['GET','POST'])
@jwt_required(optional=True)
def add_friend():
    """User adds a friend to their friend list. This adds the user as a friend of the other too."""
    net_id = get_jwt_identity()
    email = request.args.get('email', '')

    # get user via their net id
    user = User.query.filter_by(netid=net_id).first()
    # get user to add as friend via their netid
    added_friend = User.query.filter_by(email=email).first()

    # both users should be found. If not there's an error
    if not user or not added_friend:
        return jsonify({"error": "User not found"}), 404

    # User can only add friends from their pending friend list
    # Pending friends list has been discontinued
    # if added_friend not in user.pending:
    #     return jsonify({"message": "Your friend must request to be friends first"})

    elif added_friend in user.friends:
        return jsonify({"message": "You're already friends with this user!"})
    # removes user from other user's friends pending list if they're on it
    # if user in added_friend.pending:
    #     added_friend.pending.remove(user)

    # adds user to friends list, then returns
    # user.pending_friends.remove(added_friend)
    user.friends.add(added_friend)
    if user not in added_friend.friends:
        added_friend.frends.add(user)
    db.session.commit()

    return jsonify({"message": "Friend added!"})

@bp_users.route('/list_friends', methods=['GET'])
@jwt_required(optional=True)
def list_friends():
    """Get the favorited events for a given user"""
    net_id = get_jwt_identity()

    # get user via their net id
    user = User.query.filter_by(netid=net_id).first()
    print("USER ", user)

    friends = {}
    if user:
        friends = user.friends
    # print("FRIENDS ", friends)
    # get events dict
    friends_dict = [user.profile() for user in friends]
    # print("FRIENDS DICT ", friends_dict)
    return jsonify(friends_dict)

# @bp_users.route('/request_friend', methods=['GET','POST'])
# @jwt_required(optional=True)
# def request_friend():
#     """User requests to be friends with other person via email address"""
#     net_id = get_jwt_identity()
#     email = request.args.get('email', '')

#     # get user
#     user = User.query.filter_by(netid=net_id).first()
#     # get user to request friends
#     added_friend = User.query.filter_by(email=email).first()

#     # both users should be found, If not there's an error
#     if not user or not event:
#         return jsonify({"error": "User not found"}), 404

#     # Checks if user is alread a friend or is pending
#     if user in added_friend.friends:
#         return jsonify({"message": "You're already friends with this user!"})

#     elif user in added_friend.pending_friends:
#         return jsonify({"message": "Your friend request has already been sent!"})

#     # adds user to pending friends list, then returns
#     added_friend.pending_friends.add(user)
#     db.session.commit()

#     return jsonify({"message": "Friend request sent!"})


####----Helper Functions----##
def get_user(netid):
    """Getting user information from yalies.io"""
    token = app.config['API_TOKEN']
    api = yalies.API(token)

    person = api.person(filters={'netid': netid})
    print(person.raw)
    return person