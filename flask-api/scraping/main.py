# from scraping.dep_a_to_e.dep_A import get_all_events_A
# from scraping.dep_a_to_e.dep_C import get_all_events_C

from scraping.dep_a_to_z.dep_A import get_all_events_A
from scraping.dep_a_to_z.dep_B import get_all_events_B
from scraping.dep_a_to_z.dep_C import get_all_events_C


# List of functions
functions = [get_all_events_A, get_all_events_B, get_all_events_C]
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