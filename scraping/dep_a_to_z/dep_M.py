
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

def Math(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("div",{"class": "views-field views-field-titl"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split('/genetics')[1]
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
            speaker_name = soup.find('div', {'class':'field-item even'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        try:
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
        except:
            date = "TBD"
            time = "TBD"
            iso = "TBD"
        # we get the address 
        try:
        
            address = soup.find('span', {'class': 'fn'}).text.strip()
            
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
            "link": link
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Management(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'about/events')
    soup = BeautifulSoup(response.content, "html.parser")
    # get events links
    event_links = []
    events = soup.find_all('s', class_="som-row__heading-link")
    for row in events:
        link = row.find('a').get('href')
        if link:
            event_links.append(link)
    

    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('title').text.strip()
        
        # speaker
        speaker_name = soup.find('div', {'class': 'field-name-field-speaker'}).text.split(':')[-1].strip()
        try:
            # NEEDS TO BE CHECKED!
            date = soup.find('li',{'class':'time'}).text.strip().strip('at')[0]
            time = soup.find('li',{'class':'time'}).text.strip().strip('at')[1]
        except:
            date = "TBD"
            time = "TBD"
            iso = "TBD"
        try:
            
            address = soup.find('p', {'class': 'address'}).text.strip()

        except:
            address = "TBD"
        
    

         # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": speaker_name,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Music (main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    # get events links
    event_links = []
    events = soup.find_all('td', class_="views-field views-field-title")
    for row in events:
        link = row.find('a').get('href')
        if link:
            event_links.append(link)
    
    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('title').text.strip()
        
        # speaker
        speaker_name = soup.find('div', {'class': 'field-name-field-speaker'}).text.split(':')[-1].strip()
        try:
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
        except:
            date = "TBD"
            time = "TBD"
            iso = "TBD"

        try:
        
            json_str =  soup.find('script', {'type': 'application/ld+json'})
            json_data = json_str.text.strip()
            event_dict = json.loads(json_data)
            address = event_dict['location']['address']['streetAddress']
            json_data = json.dumps(event_dict)
            
        except:
            address = "TBD"
        
    

         # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": speaker_name,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link
        }
        return event
        # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events



department_parsers = {
"https://math.yale.edu/": Math,
"https://german.yale.edu/": Management,
"https://yalemusic.yale.edu/": Music

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