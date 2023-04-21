"""
This is script for getting all the events for departments starting with letter B
""""""
This is script for getting all the events for departments starting with letter B
"""
import requests
from bs4 import BeautifulSoup
import sys
from scraping.DateTime import getDate, getTime, getISO
from scraping.dep_events import all_department_links, get_dep_events
import json
import re
from datetime import datetime
from dateutil import parser


##-------------------Biological_Biomedical_SciencesDep---------------##
def Biological_Biomedical_Sciences(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split("/bbs")[1]
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
            speaker_name = soup.find('span', {'class': 'profile-detailed-info-list-item__name'}).text.strip()
        except:
            speaker_name = "TBD"


        # time and date
        # date_div = soup.find('div', {'class': 'field-name-field-event-time'})
        # date_str = date_div.find('span', {'class': 'date-display-single'})
        start_date = None
        start_time = None
        try:
            start_time = soup.find('span',{'class':'event-time__start-date'}).text.strip()
            end_time = soup.find('span',{'class':'event-time__end-date'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        try:
            start_date = soup.find('span',{'class':'event-date__month-year'}).text.strip()
            end_time = soup.find('span',{'class':'event-date__day'}).text.strip()
            date = f"{start_date} {end_time}"
        except:
            date = "TBD"

        try:
            json_str =  soup.find('script', {'type': 'application/ld+json'})
            json_data = json_str.text.strip()
            event_dict = json.loads(json_data)
            address = event_dict['location']['address']['streetAddress']
            json_data = json.dumps(event_dict)
        except:
            address = "TBD"
        date_str = date + " " + start_time if start_time is not None else date
        iso_date = getISO(date_str)

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

def Biomedical_Engineering(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'news-events/events?type=All&tid_1=1&keys=')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "views-field-title"})
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
            speaker_name = soup.find('div', {'class':'event-presenter'}).text.strip()
        except:
            speaker_name = "TBD"


        start_date = None
        start_time = None
        try:
            start_time = soup.find('span',{'class':'date-display-start'}).text.strip()
            end_time = soup.find('span',{'class':'date-display-end'}).text.strip()
            time = f"{start_time} - {end_time}"

        except:
            time = "TBD"
        try:
            date = soup.find('span',{'class':'date-display-single'}).text.strip()

        except:
            date = "TBD"

        try:
            address = soup.find('div', {'class': 'street-address'}).text.strip()

        except:
            address = "TBD"

        input_str = date
        # parse the input string using dateutil
        start_datetime = parser.parse(input_str.split(" - ")[0] + " " + input_str.split(" - ")[1])

        # format the date and start time into a single line
        formatted_datetime = start_datetime.strftime("%Y-%m-%d %H:%M")
        iso_date = getISO(formatted_datetime)

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

def Biostatistics(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
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
            speaker_name = soup.find('div', {'class':'profile-detailed-info-list-item__name'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        start_time = None
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

        date_str = date + " " + start_time if start_time is not None else date
        iso_date = getISO(date_str)

         # Event object as a dictionary
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


####---------------Get ALL Events for departments starting with letter A------####
# A dictionary of department links and functions to get events
department_parsers = {
"https://medicine.yale.edu/bbs/": Biological_Biomedical_Sciences,
"https://seas.yale.edu/": Biomedical_Engineering,
"https://ysph.yale.edu/": Biostatistics
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
