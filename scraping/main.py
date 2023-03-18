from dep_a_to_e.dep_A import get_all_events_A
from dep_a_to_e.dep_C import get_all_events_C

events_c = get_all_events_C()
events_a = get_all_events_A()
events = events_a + events_c
print(len(events))
print(events)