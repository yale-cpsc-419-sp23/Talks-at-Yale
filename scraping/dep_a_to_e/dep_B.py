"""
This is script for getting all the events for departments starting with letter B
"""
import requests
from bs4 import BeautifulSoup
import sys
from DateTime import getDate, getTime
from dep_events import all_department_links, get_dep_events
import json
import re
from datetime import datetime


##-------------------Biological_Biomedical_SciencesDep---------------##
def Biological_Biomedical_Sciences(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    for div in all_links:
        link = div.find('a').get('href')
        event_links.append(link)


    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('h2', {'class': 'event-list-item__title'}).text.strip()

        # speaker
        speaker_name = soup.find('div', {'class': 'event-speaker-name'})

        # speaker title
       
        speaker_title = None

        # time and date
        date_div = soup.find('div', {'class': 'field-name-field-event-time'})
        date_str = date_div.find('span', {'class': 'date-display-single'})
        

        if date_str.has_attr('content'):
            content_attr = date_str['content']
            iso = content_attr
            date = getDate(content_attr)
            time = getTime(content_attr)
        else:
            date_str = date_div.find('span', {'class': 'date-display-start'})
            content_attr = date_str['content']
            iso = content_attr
            date = getDate(content_attr)
            time = getTime(content_attr)

        # adress:
        # address = 


         # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": speaker_title,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


####---------------Get ALL Events for departments starting with letter A------####
# A dictionary of department links and functions to get events
department_parsers = {
"https://medicine.yale.edu/bbs/",Biological_Biomedical_Sciences
#"https://seas.yale.edu/departments/biomedical-engineering", Biomedical_Engineering
# "https://ysph.yale.edu/public-health-research-and-practice/department-research/biostatistics/",Biostatistics
}

def get_all_events_B():
    """A function that returns all events for departments starting with letter A"""
    links = all_department_links()
    all_events = []
    calendar = "calendar"
    if links:
        for name, url in links.items():
            if url in department_parsers:
                department_parser = department_parsers[url]
                department_events = department_parser(url, calendar, name)
                all_events.extend(department_events)
        return all_events

