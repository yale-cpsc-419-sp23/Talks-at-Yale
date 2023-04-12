"""
This is script for getting all the events for departments starting with letter D
"""

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

def Earth_Planetary_Sciences(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("div",{"class": "views-field views-field-title"})
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
            speaker_name = soup.find('div', {'class':'speaker_name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"
            
        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('span',{'class': 'date-display-single'}).text.strip()

        except:
            date = "TBD"
        # we get the address 
        try:
           address = soup.find('span',{'class': 'fn'})
        except:
            address = "TBD"


        # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": "TBD",
            "date": date,
            "time": time,
            "location": address,
            "iso_date": "TBD",
        }
        return event
    
    events = get_dep_events(main_url, get_event, event_links)
    return events


def East_Asian_Languages_Literatures(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("div",{"class": "views-field views-field-title"})
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
            speaker_name = soup.find('div', {'class':'speaker_name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"
            
        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('span',{'class': 'date-display-single'}).text.strip()

        except:
            date = "TBD"
        # we get the address 
        try:
            address = soup.find('span',{'class': 'fn'})
        except:
            address = "TBD"


        # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": "TBD",
            "date": date,
            "time": time,
            "location": address,
            "iso_date": "TBD",
        }
        return event
    
    events = get_dep_events(main_url, get_event, event_links)
    return events

def East_Asian_Studies(main_url, calendar, dep):
    """Getting African American studies department's events"""
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
            speaker_name = soup.find('div', {'class':'field field-name-field-speaker field-type-text field-label-hidden clearfix'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        try:
            time_div = soup.find('div', {'class': 'field field-name-field-event-time field-type-datetime field-label-hidden'})
            start_time = time_div.find('span',{'class':'date-display-start'}).text.strip()
            end_time = time_div.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"
        except:
            time = "TBD"
        # we get the date of the event
        try:
            date_div = soup.find('div', {'class': 'field field-name-field-event-time field-type-datetime field-label-hidden'})
            date = date_div.find('span', {'class': 'date-display-single'}).text.strip()
        except:
            date = "TBD"
        # we get the address 
        try:
            address = soup.find('span',{'class': 'fn'}).text.strip() + soup.find('div',{'class': 'street-address'}).text.strip()
        except:
            address = "TBD"


        # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": "TBD",
            "date": date,
            "time": time,
            "location": address,
            "iso_date": "TBD",
        }
        return event
    
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Ecology_Evolutionary_Biology(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("div",{"class": "views-field views-field-title"})
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
            speaker_name = soup.find('div', {'class':'speaker_name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        try:
            time = soup.find('span',{'class': 'date-display-single'}).text.strip()
            
        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('span',{'class': 'date-display-single'}).text.strip()

        except:
            date = "TBD"
        # we get the address 
        try:
           address = soup.find('span',{'class': 'fn'})
        except:
            address = "TBD"


        # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": "TBD",
            "date": date,
            "time": time,
            "location": address,
            "iso_date": "TBD",
        }
        return event
    
    events = get_dep_events(main_url, get_event, event_links)
    return events
department_parsers = {
"https://earth.yale.edu/": Earth_Planetary_Sciences,
"https://eall.yale.edu/": East_Asian_Languages_Literatures,
"https://ceas.yale.edu/": East_Asian_Studies,
"https://eeb.yale.edu/": Ecology_Evolutionary_Biology,
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