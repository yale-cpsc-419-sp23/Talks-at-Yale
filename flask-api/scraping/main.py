from scraping.dep_a_to_e.dep_A import get_all_events_A
from scraping.dep_a_to_e.dep_C import get_all_events_C


# List of functions
functions = [get_all_events_A, get_all_events_C]
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