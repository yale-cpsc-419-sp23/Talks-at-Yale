"""api endpoints dealing with events such as getting events will go in this file"""
from flask import request, jsonify
from datetime import datetime
from sqlalchemy import or_
from app.events import bp_events
from app.models import Event

@bp_events.route('/search', methods=['GET'])
def search():
    """Search an event"""
    # get search term
    search_term = request.args.get('search_term', '')

    # Query the database
    events = Event.query.filter(
        or_(
            Event.title.ilike(f'%{search_term}%'),
            Event.type.ilike(f'%{search_term}%'),
            Event.speaker.ilike(f'%{search_term}%'),
            Event.speaker_title.ilike(f'%{search_term}%'),
            Event.host.ilike(f'%{search_term}%'),
            Event.department.ilike(f'%{search_term}%'),
            Event.bio.ilike(f'%{search_term}%'),
            Event.description.ilike(f'%{search_term}%'),
            Event.location.ilike(f'%{search_term}%'),
        )
    ).all()

    events_dict = [event.to_dict() for event in events]
    events_json = update_dates(events_dict)
    # return json data
    return jsonify(events_json)


@bp_events.route('/filter', methods=['GET'])
def event_filter():
    """Search an event"""
    # get search term
    search_term = request.args.get('department', '')
    print(search_term)
    # Query the database
    events = Event.query.filter_by(department = search_term).all()
    print(len(events))
    events_dict = [event.to_dict() for event in events]
    events_json = update_dates(events_dict)
    # return json data
    return jsonify(events_json)

def convert_date(date_str):
    """Convert date in a format to be used in the frontend"""
    # Parse the date string
    date_obj = datetime.strptime(date_str, "%Y/%m/%d")

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

def update_dates(dicts_list):
    """Updates the dates in the list of the dicts in a formatted way"""
    for event_dict in dicts_list:
        date_str = event_dict.get('date')
        if date_str:
            formatted_date = convert_date(date_str)
            event_dict['formatted_date'] = formatted_date
    return dicts_list
