# from scraping.dep_a_to_e.dep_A import get_all_events_A
# from scraping.dep_a_to_e.dep_C import get_all_events_C

from scraping.dep_a_to_z.dep_A import get_all_events_A
from scraping.dep_a_to_z.dep_B import get_all_events_B
from scraping.dep_a_to_z.dep_C import get_all_events_C
from scraping.dep_a_to_z.dep_D import get_all_events_D
from scraping.dep_a_to_z.dep_E import get_all_events_E
from scraping.dep_a_to_z.dep_F import get_all_events_F
from scraping.dep_a_to_z.dep_G import get_all_events_G
from scraping.dep_a_to_z.dep_H import get_all_events_H
from scraping.dep_a_to_z.dep_I import get_all_events_I
from scraping.dep_a_to_z.dep_J import get_all_events_J
from scraping.dep_a_to_z.dep_W import get_all_events_W
from scraping.dep_a_to_z.dep_U import get_all_events_U
from scraping.dep_a_to_z.dep_S import get_all_events_S
from scraping.dep_a_to_z.dep_R import get_all_events_R
from scraping.dep_a_to_z.dep_O import get_all_events_O
from scraping.dep_a_to_z.dep_N import get_all_events_N


# List of functions
functions = [get_all_events_A, get_all_events_B, get_all_events_C, get_all_events_D, get_all_events_E, get_all_events_F, get_all_events_G, get_all_events_H, get_all_events_I, get_all_events_J, get_all_events_N, get_all_events_O, get_all_events_R, get_all_events_S, get_all_events_U, get_all_events_W]
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