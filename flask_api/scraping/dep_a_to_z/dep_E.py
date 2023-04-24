"""
This is script for getting all the events for departments starting with letter D
"""

"""
This is script for getting all the events for departments starting with letter D
"""

import requests
from bs4 import BeautifulSoup
import sys
from flask_api.scraping.DateTime import getDate, getTime, getISO
from flask_api.scraping.dep_events import all_department_links, get_dep_events
import json
import re
from datetime import datetime
import datetime
import time

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
        iso = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('span',{'class': 'date-display-single'}).text.strip()
            iso = getISO(date)

        except:
            date = "TBD"
        # we get the address
        try:
           address = soup.find('span',{'class': 'fn'}).text.strip()
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
            "iso_date": iso,
            "link": link,
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
        iso = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('span',{'class': 'date-display-single'}).text.strip()
            iso = getISO(date)

        except:
            date = "TBD"
        # we get the address
        try:
            address = soup.find('span',{'class': 'fn'}).text.strip()
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
            "iso_date": iso,
            "link": link,
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
        iso = None
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
            iso = getISO(date)
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
            "iso_date": iso,
            "link": link,
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
        iso = None
        try:
            date = soup.find('span',{'class': 'date-display-single'}).text.strip()
            iso=getISO(date)

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
            "iso_date": iso,
            "link": link,
        }
        return event


def economics(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "node-teaser__event-series"})
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
            speaker_name = soup.find('div', {'class':'node-teaser__heading'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        iso = None
        try:
            time = soup.find('div',{'class': 'node-teaser__event-date-additional'}).text.strip()

        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('div',{'class': 'node-teaser__event-start-date'}).text.strip()
            iso = getISO(iso)
        except:
            date = "TBD"
        # we get the address
        try:
           address = soup.find('div',{'class': 'node-teaser__address-label'}).text.strip()
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
            "iso_date": iso,
            "link": link,
        }
        return event
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Electrical_Engineering(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'news-events/events?type=All&tid_1=3&keys=')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links

    all_links = soup.find_all("div",{"class": "views-field-title"})
    try:
        for div in all_links:
            link = div.find('a')['href']
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
            speaker_name = soup.find('div', {'class':'event-presenter'}).text.strip()
        except:
            speaker_name = "TBD"


        start_date = None
        iso = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        try:
            date = soup.find('span',{'class':'date-display-single'}).text.strip()
            iso = getISO(iso)

        except:
            date = "TBD"

        try:
            address = soup.find('div', {'class': 'street-address'}).text.strip()

        except:
            address = ""
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events

def Emergency_Medicine(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split('/emergencymed')[1]
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
            speaker_name = soup.find('span', {'class':'profile-detailed-info-list-item__name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        iso = None
        try:
            start_time = soup.find('span',{'class':'event-time__start-date'}).text.strip()
        except:
            start_time = "TBD"
        try:
            end_time = soup.find('span',{'class':'event-time__end-date'}).text.strip()
        except:
            end_time = "TBD"
        time = f"{start_time} - {end_time}"

        # we get the date of the event
        try:
            year = soup.find('span', {'class': {'event-date__month-year'}}).text.strip()
            date__day = soup.find('span', {'class': {'event-date__day-of-week'}}).text.strip()
            event_date__day= soup.find('span', {'class': {'event-date__day'}}).text.strip()
            date = f"{date__day} {event_date__day} {year}"
            iso = getISO(date)

        except:
            date = "TBD"
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
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events

def Engineering_Applied_Science(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'news-events/events?type=All&tid_1=3&keys=')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links

    all_links = soup.find_all("div",{"class": "views-field-title"})
    try:
        for div in all_links:
            link = div.find('a')['href']
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
            speaker_name = soup.find('div', {'class':'event-presenter'}).text.strip()
        except:
            speaker_name = "TBD"


        start_date = None
        iso = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        try:
            date = soup.find('span',{'class':'date-display-single'}).text.strip()
            iso = getISO(date)

        except:
            date = "TBD"

        try:
            address = soup.find('div', {'class': 'street-address'}).text.strip()

        except:
            address = ""
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events

def English_Language_Literature(main_url, calendar, dep):
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
            name_div = soup.find('div', {'class': 'field-name-field-speaker-name'})
            speaker_name = name_div.find('div', {'class': 'field-item even'}).text.strip()

            # speaker title
            speaker_div = soup.find('div', {'class': 'field-name-field-speaker-title'})
            speaker_title = speaker_div.find('div', {'class': 'field-item even'}).text.strip()
        except:
            speaker_title = "TBD"
            speaker_div = "TBD"
            speaker_name = "TBD"

        # time and date
        try:
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
            time = "TBD"
            date = "TBD"
        try:
            address = soup.find('span',{'class': 'fn'}).text.strip()
        except:
            address = "TBD"

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
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Environmental_Health_Sciences(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + '/yale-school-of-public-health-event-calendar/')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
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
            title = ""

            # speaker
        try:
            speaker_name = soup.find('span', {'class':'profile-detailed-info-list-item__name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        iso = None
        try:
            start_time = soup.find('span',{'class':'event-time__start-date'}).text.strip()
            end_time = soup.find('span',{'class':'event-time__end-date'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        # we get the date of the event
        try:
            year = soup.find('span', {'class': {'event-date__month-year'}}).text.strip()
            date__day = soup.find('span', {'class': {'event-date__day-of-week'}}).text.strip()
            event_date__day= soup.find('span', {'class': {'event-date__day'}}).text.strip()
            date = f"{date__day} {event_date__day} {year}"
            iso = getISO(date)

        except:
            date = "TBD"
        # we get the address
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
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events

def Epidemiology_Microbial_Diseases(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get('https://ysph.yale.edu/public-health-research-and-practice/department-research/epidemiology-of-microbial-diseases/events/')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
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
            title = ""

            # speaker
        try:
            speaker_name = soup.find('span', {'class':'profile-detailed-info-list-item__name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        iso = None
        try:
            start_time = soup.find('span',{'class':'event-time__start-date'}).text.strip()
            end_time = soup.find('span',{'class':'event-time__end-date'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        # we get the date of the event
        try:
            year = soup.find('span', {'class': {'event-date__month-year'}}).text.strip()
            date__day = soup.find('span', {'class': {'event-date__day-of-week'}}).text.strip()
            event_date__day= soup.find('span', {'class': {'event-date__day'}}).text.strip()
            date = f"{date__day} {event_date__day} {year}"
            iso = getISO(date)

        except:
            date = "TBD"
        # we get the address
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
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Ethnicity_Race_Migration(main_url, calendar, dep):
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
        iso = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('span',{'class': 'date-display-single'}).text.strip()
            iso = getISO(date)

        except:
            date = "TBD"
        # we get the address
        try:
           address = soup.find('span',{'class': 'fn'}).text.strip()
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
            "iso_date": iso,
            "link": link,
        }
        return event

    events = get_dep_events(main_url, get_event, event_links)
    return events

def European_Russian_Studies(main_url, calendar, dep):
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
            div = soup.find('div', {'class':'field field-name-field-speaker-performer field-type-text field-label-above'})
            speaker_name = div.find('div', {'class':'field-item even'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        iso = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('span',{'class': 'date-display-single'}).text.strip()
            iso = getISO(date)

        except:
            date = "TBD"
        # we get the address
        try:
           address = soup.find('span',{'class': 'fn'}).text.strip()
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
            "iso_date": iso,
            "link": link,
        }
        return event

    events = get_dep_events(main_url, get_event, event_links)
    return events

def Experimental_Pathology(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + '/news/calendar/')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split('/pathology')[1]
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
            speaker_name = soup.find('span', {'class':'profile-detailed-info-list-item__name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        iso_date = None
        try:
            start_time = soup.find('span',{'class':'event-time__start-date'}).text.strip()
        except:
            start_time = "TBD"
        try:
            end_time = soup.find('span',{'class':'event-time__end-date'}).text.strip()
        except:
            end_time = "TBD"
        time = f"{start_time} - {end_time}"

        # we get the date of the event
        try:
            year = soup.find('span', {'class': {'event-date__month-year'}}).text.strip()
            date__day = soup.find('span', {'class': {'event-date__day-of-week'}}).text.strip()
            event_date__day= soup.find('span', {'class': {'event-date__day'}}).text.strip()
            date = f"{date__day} {event_date__day} {year}"

        except:
            date = "TBD"
        try:
            iso_date = datetime.datetime(year=year, month=event_date__day, hour=0, minute=0, second=0)
            return iso_date
            # Convert datetime object to ISO 8601 format
            # iso_date = dt.isoformat()
        except:
            iso_date= "TBD"
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
            "iso_date": iso_date,
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events
department_parsers = {
"https://earth.yale.edu/": Earth_Planetary_Sciences,
"https://eall.yale.edu/": East_Asian_Languages_Literatures,
"https://ceas.yale.edu/": East_Asian_Studies,
"https://eeb.yale.edu/": Ecology_Evolutionary_Biology,
"https://economics.yale.edu/": economics,
"https://seas.yale.edu/": Electrical_Engineering,
"https://medicine.yale.edu/emergencymed/": Emergency_Medicine,
"https://seas.yale.edu/": Engineering_Applied_Science,
"https://english.yale.edu/": English_Language_Literature,
"https://ysph.yale.edu": Environmental_Health_Sciences,
"https://ysph.yale.edu/": Epidemiology_Microbial_Diseases,
"https://erm.yale.edu/": Ethnicity_Race_Migration,
"https://europeanstudies.macmillan.yale.edu/" : European_Russian_Studies,
"https://medicine.yale.edu/pathology": Experimental_Pathology


}

def get_all_events_E():
    """A function that returns all events for departments starting with letter A"""
    links = all_department_links()
    all_events = []
    calendar = "calendar"
    if links:
        for name, url in links.items():
            if url in department_parsers:
                department_parser = department_parsers[url]
                department_events = department_parser(url, calendar, name)
                if department_events is not None:
                    all_events.extend(department_events)
        return all_events
