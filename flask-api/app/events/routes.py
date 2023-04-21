"""api endpoints dealing with events such as getting events will go in this file"""
from flask import request, jsonify
from datetime import datetime
from sqlalchemy import or_, and_
from app.events import bp_events
from app.models import Event, User
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import distinct


@bp_events.route('/')
@bp_events.route('/search', methods=['GET'])
def search():
    """Search an event"""
    # get search term
    search_term = request.args.get('search_term', '')
    print(search_term)


    # get selected department
    selected_dept = request.args.get('department', 'All Departments')
    print(selected_dept)

    # get selected status
    selected_status = request.args.get('status', 'Upcoming')
    print(selected_status)

    # get selected sort by
    selected_sort = request.args.get('sort', 'Date')
    print(selected_sort)

    # define the mapping of sort options to database columns
    sort_mapping = {
        'Date': Event.iso_date,
        'Title': Event.title,
        'Department': Event.department
    }
    # check if the selected sort option is valid
    if selected_sort not in sort_mapping:
        selected_sort = 'Date'

     # Query the database
    if selected_dept == 'All Departments' and search_term != '':
        if selected_status == 'All Dates':
            events = Event.query.filter(
                or_(
                    Event.title.ilike(f'%{search_term}%'),
                    Event.type.ilike(f'%{search_term}%'),
                    Event.speaker.ilike(f'%{search_term}%'),
                    Event.speaker_title.ilike(f'%{search_term}%'),
                    Event.host.ilike(f'%{search_term}%'),
                    Event.bio.ilike(f'%{search_term}%'),
                    Event.description.ilike(f'%{search_term}%'),
                    Event.location.ilike(f'%{search_term}%'),
                )
            ).order_by(sort_mapping[selected_sort]).all()
        else:
            now = datetime.now()
            events = Event.query.filter(
                and_(
                    Event.iso_date >= now.strftime('%Y-%m-%d') if selected_status == 'Upcoming' else Event.iso_date < now.strftime('%Y-%m-%d'),
                    or_(
                        Event.title.ilike(f'%{search_term}%'),
                        Event.type.ilike(f'%{search_term}%'),
                        Event.speaker.ilike(f'%{search_term}%'),
                        Event.speaker_title.ilike(f'%{search_term}%'),
                        Event.host.ilike(f'%{search_term}%'),
                        Event.bio.ilike(f'%{search_term}%'),
                        Event.description.ilike(f'%{search_term}%'),
                        Event.location.ilike(f'%{search_term}%'),
                    )
                )
            ).order_by(sort_mapping[selected_sort]).all()
    elif search_term == '' and selected_dept != 'All Departments':
        if selected_status == 'All Dates':
            events = Event.query.filter(
                Event.department == selected_dept
            ).order_by(sort_mapping[selected_sort]).all()
        else:
            now = datetime.now()
            events = Event.query.filter(
                and_(
                    Event.iso_date >= now.strftime('%Y-%m-%d') if selected_status == 'Upcoming' else Event.iso_date < now.strftime('%Y-%m-%d'),
                    Event.department == selected_dept
                )
            ).order_by(sort_mapping[selected_sort]).all()
    elif search_term == '' and selected_dept == "All Departments":
        if selected_status == 'All Dates':
            events = Event.query.order_by(sort_mapping[selected_sort]).all()
        else:
            now = datetime.now()
            events = Event.query.filter(
                and_(
                    Event.iso_date >= now.strftime('%Y-%m-%d') if selected_status == 'Upcoming' else Event.iso_date < now.strftime('%Y-%m-%d')
                )
            ).order_by(sort_mapping[selected_sort]).all()
    else:
        if selected_status == 'All Dates':
            events = Event.query.filter(
                and_(
                    Event.department == selected_dept,
                    or_(
                        Event.title.ilike(f'%{search_term}%'),
                        Event.type.ilike(f'%{search_term}%'),
                        Event.speaker.ilike(f'%{search_term}%'),
                        Event.speaker_title.ilike(f'%{search_term}%'),
                        Event.host.ilike(f'%{search_term}%'),
                        Event.bio.ilike(f'%{search_term}%'),
                        Event.description.ilike(f'%{search_term}%'),
                        Event.location.ilike(f'%{search_term}%'),
                    )
                )
            ).order_by(sort_mapping[selected_sort]).all()
        else:
            now = datetime.now()
            events = Event.query.filter(
                and_(
                    Event.iso_date >= now.strftime('%Y-%m-%d') if selected_status == 'Upcoming' else Event.iso_date < now.strftime('%Y-%m-%d'),
                    Event.department == selected_dept,
                    or_(
                        Event.title.ilike(f'%{search_term}%'),
                        Event.type.ilike(f'%{search_term}%'),
                        Event.speaker.ilike(f'%{search_term}%'),
                        Event.speaker_title.ilike(f'%{search_term}%'),
                        Event.host.ilike(f'%{search_term}%'),
                        Event.bio.ilike(f'%{search_term}%'),
                        Event.description.ilike(f'%{search_term}%'),
                        Event.location.ilike(f'%{search_term}%'),
                    )
                )
            ).order_by(sort_mapping[selected_sort]).all()

    # for item in events:
    #     print(item.iso_date)

    events_dict = [event.to_dict() for event in events]
    events_json = update_dates(events_dict)
    # return json data
    return jsonify(events_json)
# @bp_events.route('/filter', methods=['GET'])
# def event_filter():
#     """Search an event"""
#     # get search term
#     dep = request.args.get('department', '')
#     loc = request.args.get('location', '')
#     start_date = request.args.get('start_date', '')
#     end_date = request.args.get('end_date', '2050-01-01')       # "hopefully no one will be alive by then" -github copilot
#     print(dep)
#     # Query the database
#     events = Event.query.filter(Event.iso_date > start_date, Event.iso_date < end_date, department = dep, location=loc).all()
#     print(len(events))
#     events_dict = [event.to_dict() for event in events]
#     events_json = update_dates(events_dict)
#     # return json data
#     return jsonify(events_json)

@bp_events.route('/add_favorite', methods=['GET','POST'])
@jwt_required()
def add_favorite():
    """Add favorite event"""
    net_id = get_jwt_identity()
    event_id = request.args.get('event_id', '')
    # get user
    user = User.query.filter_by(netid=net_id).first()
    # get event
    event = Event.query.filter_by(id=event_id).first()

    if not user or not event:
        print("Nothing found.")
        return jsonify({"error": "User or event not found"}), 404

    # Check if the event is already in the user's favorite events
    if event in user.favorite_events:
        print("Event already exist")
        return jsonify({"error": "Event already in favorites"}), 400

    # Add favorite event
    user.favorite_events.append(event)
    db.session.commit()
    print("event added to fav!")
    return jsonify({"ok": "Event added to your favorites"}), 200

@bp_events.route('/remove_favorite', methods=['GET','POST'])
@jwt_required()
def remove_favorite():
    """Remove favorite event"""
    net_id = get_jwt_identity()
    event_id = request.args.get('event_id', '')
    # get user
    user = User.query.filter_by(netid=net_id).first()
    # get event
    event = Event.query.filter_by(id=event_id).first()

    if not user or not event:
        return jsonify({"error": "User or event not found"}), 404

    # Remove favorite event only if it's in the user's favorites
    if event in user.favorite_events:
        user.favorite_events.remove(event)
        db.session.commit()
    else:
        return jsonify({"error": "Event not in favorites"}), 400

    return jsonify({"message": "Event removed from favorites"})

@bp_events.route('/favorite_events', methods=['GET'])
@jwt_required(optional=True)
def favorite_events():
    """Get the favorited events for a given user"""
    net_id = get_jwt_identity()
    # get user
    user = User.query.filter_by(netid=net_id).first()

    favorite_events = {}
    if user:
        favorite_events = user.favorite_events
    # get events dict
    events_dict = [event.to_dict() for event in favorite_events]

    return jsonify(events_dict)

@bp_events.route('/events_status', methods=['GET'])
@jwt_required(optional=True)
def events_status():
    """Get the favorited events for a given user"""
    net_id = get_jwt_identity()
    # get user
    user = User.query.filter_by(netid=net_id).first()

    # ids
    favorite_events_ids = None
    if user:
        favorite_events_ids = [favorite.id for favorite in user.favorite_events]
    else:
        return jsonify({'IDS':[]})

    response = {'IDS': favorite_events_ids}
    print(response)
    return jsonify(response)



# @bp_events.route('/popup/<int:event_id>', methods=['GET'])
# def get_event(event_id):
#     """Get an event by ID"""
#     event = Event.query.filter_by(id=event_id).first()

#     if not event:
#         return jsonify({"error": "Event not found"}), 404

#     event_dict = event.to_dict()
#     event_dict = update_dates([event_dict])

#     return jsonify(event_dict)

@bp_events.route('/departments', methods=['GET'])
def get_departments():
    unique_departments = db.session.query(distinct(Event.department)).all()

    # extract department names
    department_names = [row[0] for row in unique_departments]
    return jsonify(department_names)

@bp_events.route('/clean_database', methods=['GET'])
def clean_database():
    "Cleaning the database"
    # Find all events without iso_date or with iso_date "TBD"
    events_to_delete = Event.query.filter(or_(Event.iso_date == None, Event.iso_date == "TBD", Event.title == None)).all()

    # Delete the events from the database
    for event in events_to_delete:
        db.session.delete(event)

    # Commit the changes
    db.session.commit()

    # Return a success message
    return jsonify({"message": "All events without iso_date or with iso_date 'TBD' have been deleted from the database"}), 200


####-----------Helper functions-----------------####
def convert_date(date_str):
    """Convert date in a format to be used in the frontend"""
    try:
        # Parse the date string
        date_obj = datetime.fromisoformat(date_str)

        # Get the formatted date components
        week_day = date_obj.strftime("%a")
        exact_date = date_obj.strftime("%d")
        month = date_obj.strftime("%b")

        # Return the date components as a dictionary
        return {
            "week_day": week_day,
            "exact_date": exact_date,
            "month": month
        }
    except:
        return{
            "week_day": "TBD",
            "exact_date": "TBD",
            "month": "TBD"
        }

def convert_date_long(date_str):
    """Convert date in a format to be used in the frontend"""
    try:
        # Parse the date string
        date_obj = datetime.fromisoformat(date_str)

        # Get the formatted date components
        week_day = date_obj.strftime("%A")
        exact_date = date_obj.strftime("%d")
        month = date_obj.strftime("%B")

        # Return the formatted date string
        return f"{week_day}, {month} {exact_date}, {date_obj.year}"
    except:
        return "TBD"

def update_dates(dicts_list):
    """Updates the dates in the list of the dicts in a formatted way"""
    for event_dict in dicts_list:
        date_str = event_dict.get('iso')
        if date_str:
            formatted_date = convert_date(date_str)
            long_date = convert_date_long(date_str)
            event_dict['formatted_date'] = formatted_date
            event_dict['long_date'] = long_date
    return dicts_list
