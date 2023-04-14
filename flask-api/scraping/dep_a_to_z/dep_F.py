"""
This is script for getting all the events for departments starting with letter D
"""

import requests
from bs4 import BeautifulSoup
import sys
from DateTime import getDate, getTime
from dep_events import all_department_links, get_dep_events
import json
import re
from datetime import datetime

def Film_Media_Studies(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'calendar/month')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    # get events links
    all_links =soup.find_all("td",{"class": "views-field views-field-title"})

    try:
        for div in all_links:
            link = div.find('a').get('href')
            event_links.append(link)
    except:
        event_links = []
    # A function that goes to each link and gets the events details
    def get_event(link):

        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

       # title
        try:
            title = soup.find('title').text.strip()
        except:
            title = "TBD"

            # speaker
        try:
            speaker_name = soup.find('span', {'class':'event-speaker-name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        # time and date
        date_div = soup.find('div', {'class': 'field field-name-field-event-time field-type-datetime field-label-above'})
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
        # we get the address
        try:

            json_str =  soup.find('script', {'type': 'application/ld+json'})
            json_data = json_str.text.strip()
            event_dict = json.loads(json_data)
            address = event_dict['location']['address']['streetAddress']
            json_data = json.dumps(event_dict)

        except:
            address = "TBD"

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": None,
            "link" : link
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Forestry_Environmental_Studies(main_url, calendar, dep):
    """Getting Forestry_Environmental_Studies department's events THIS ONE IS SHIT!"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    # get events links
    all_links =soup.find_all("td",{"class": "views-field views-field-title"})

    try:
        for div in all_links:
            link = div.find('a').get('href')
            event_links.append(link)
    except:
        event_links = []
    # A function that goes to each link and gets the events details
    def get_event(link):

        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

       # title
        try:
            title = soup.find('title').text.strip()
        except:
            title = "TBD"

            # speaker
        try:
            speaker_name = soup.find('span', {'class':'event-speaker-name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        # time and date
        try:
            date_div = soup.find('div', {'class': 'field field-name-field-event-time field-type-datetime field-label-above'})
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
        except:
            iso = "TBD"
            date = "TBD"
            time = "TBD"
        # we get the address
        try:

            json_str =  soup.find('script', {'type': 'application/ld+json'})
            json_data = json_str.text.strip()
            event_dict = json.loads(json_data)
            address = event_dict['location']['address']['streetAddress']
            json_data = json.dumps(event_dict)

        except:
            address = "TBD"

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link" : link
        }
        return event
        # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events



def French(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    # get events links
    all_links =soup.find_all("td",{"class": "views-field views-field-title"})

    try:
        for div in all_links:
            link = div.find('a').get('href')
            event_links.append(link)
    except:
        event_links = []
    # A function that goes to each link and gets the events details
    def get_event(link):

        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

       # title
        try:
            title = soup.find('title').text.strip()
        except:
            title = "TBD"

            # speaker
        try:
            speaker_name = soup.find('span', {'class':'event-speaker-name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        # time and date
        date_div = soup.find('div', {'class': 'field field-name-field-event-time field-type-datetime field-label-above'})
        date_str = date_div.find('span', {'class': 'date-display-start'})

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
        # we get the address
        try:

            address = soup.find('span', {'class':'fn'})

        except:
            address = "TBD"

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": None,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


department_parsers = {
"https://filmstudies.yale.edu/": Film_Media_Studies,
"https://environment.yale.edu/": Forestry_Environmental_Studies,
"https://french.yale.edu/": French
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
        