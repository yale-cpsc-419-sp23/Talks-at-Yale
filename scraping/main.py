from dep_a_to_e.dep_A import Astronomy, african_studies,anesthesiology,Applied_Physics, applied_mathematics,Architecture
# from scraping.dep_a_to_e.dep_C import get_all_events_C
from dep_a_to_e.dep_B import Biological_Biomedical_Sciences


# List of functions
# events = african_studies("https://african.macmillan.yale.edu/", "calendar/", "african_studies")
# events1 = anthropology("https://anthropology.yale.edu/", "calendar/", "anthropology")
events2 = Architecture("https://americanstudies.yale.edu/", "calendar/", "american_studies")
#events2 = Biological_Biomedical_Sciences("https://medicine.yale.edu/bbs/", "calendar/", "Biological_Biomedical_Sciences")

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