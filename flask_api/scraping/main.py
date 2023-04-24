# from scraping.dep_a_to_e.dep_A import get_all_events_A
# from scraping.dep_a_to_e.dep_C import get_all_events_C

from flask_api.scraping.dep_a_to_z.dep_A import get_all_events_A
from flask_api.scraping.dep_a_to_z.dep_B import get_all_events_B
from flask_api.scraping.dep_a_to_z.dep_C import get_all_events_C
from flask_api.scraping.dep_a_to_z.dep_D import get_all_events_D
from flask_api.scraping.dep_a_to_z.dep_E import get_all_events_E
from flask_api.scraping.dep_a_to_z.dep_F import get_all_events_F
from flask_api.scraping.dep_a_to_z.dep_G import get_all_events_G
from flask_api.scraping.dep_a_to_z.dep_H import get_all_events_H
from flask_api.scraping.dep_a_to_z.dep_I import get_all_events_I
from flask_api.scraping.dep_a_to_z.dep_J import get_all_events_J
from flask_api.scraping.dep_a_to_z.dep_W import get_all_events_W
from flask_api.scraping.dep_a_to_z.dep_U import get_all_events_U
from flask_api.scraping.dep_a_to_z.dep_S import get_all_events_S
from flask_api.scraping.dep_a_to_z.dep_R import get_all_events_R
from flask_api.scraping.dep_a_to_z.dep_O import get_all_events_O
from flask_api.scraping.dep_a_to_z.dep_N import get_all_events_N

# List of functions
functions = [get_all_events_G]
def all_events():
    # a list of all events
    events = []
    for func in functions:
        sub_events = func()
        events.extend(sub_events)
    return events

# getting all events
# events = all_events()
# print(len(events))
# print(events)