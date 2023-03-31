from dep_a_to_e.dep_A import anesthesiology,Applied_Physics
# from scraping.dep_a_to_e.dep_C import get_all_events_C


# List of functions
# events = anesthesiology("https://medicine.yale.edu/anesthesiology/", "calendar/", "anesthesiology")
# events1 = anthropology("https://anthropology.yale.edu/", "calendar/", "anthropology")
events2 = Applied_Physics("https://applied.math.yale.edu/", "calendar/", "anthropology")
# print(events)
# print("\n")
print(events2)

# functions = [get_all_events_A, get_all_events_C]
# def all_events():
#     # a list of all events
#     events = []
#     for func in functions:
#         sub_events = func()
#         events.extend(sub_events)
#     return events

# getting all events
# events = all_events()
# print(len(events))
# print(events)