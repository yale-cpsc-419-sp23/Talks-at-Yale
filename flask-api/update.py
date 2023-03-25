import schedule
import time
from app import app, db
from app.models import Event
from scraping.main import all_events

def update_events():
    "A functions that updates events in the database"
    events = all_events()
    # counter
    counter = 0
    # loop through each event
    with app.app_context():
        for event_dict in events:
            # event instance
            event = Event()

            # set properties
            event.title = event_dict['title']
            event.speaker = event_dict.get('speaker')
            event.speaker_title = event_dict.get('speaker_title')
            event.host = event_dict.get('host')
            event.department = event_dict.get('department')
            event.date = event_dict['date']
            event.time = event_dict['time']
            event.iso_date = event_dict['iso_date']
            event.location = event_dict.get('location')
            event.bio = event_dict.get('bio')
            event.description = event_dict.get('description')
            event.type = event_dict.get('type')

            # generate hash for event
            event.event_hash = event.generate_hash()

            if not event.event_exists(event.title, event.date, event.time, event.iso_date):
                # add event to database
                db.session.add(event)
                counter += 1
        # commit the changes
        db.session.commit()
    print(f'Added Events: {counter} events.')

def update_events_periodic():
    # run every hour
    schedule.every().day.do(update_events)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    update_events_periodic()