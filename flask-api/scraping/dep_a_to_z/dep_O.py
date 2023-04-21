
"""
This is script for getting all the events for departments starting with letter D
"""

import requests
from bs4 import BeautifulSoup
import sys
from scraping.DateTime import getDate, getTime, getISO
from scraping.dep_events import all_department_links, get_dep_events
import json
import re
from datetime import datetime


def Obstetrics_Gynecology_Reproductive_Sciences(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    print(main_url+calendar)
    links_cont = soup.find('div', {'class': 'page__content-container'})
    links_div = links_cont.find('div', {'class': 'event-list__groups-container'})
    all_links =links_div.find_all("section",{"class": "event-list__group"})
    for div in all_links:
        link = div.find('a').get('href')
        root = 'https://medicine.yale.edu'
        event_links.append(root + link)

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
        try:
            description = soup.find('div', {'class': 'event-details-info__description'}).text.strip()
        except:
            description = None

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
            "description": description,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events




department_parsers = {
"https://medicine.yale.edu/obgyn/": Obstetrics_Gynecology_Reproductive_Sciences

}

def get_all_events_O():
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
