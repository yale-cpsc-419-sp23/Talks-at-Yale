
"""
This is script for getting all the events for departments starting with letter D
"""

import requests
from bs4 import BeautifulSoup
import sys
from flask_api.scraping.DateTime import getDate, getTime
from flask_api.scraping.dep_events import all_department_links, get_dep_events
import json
import re
from datetime import datetime


def Renaissance_Studies(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    # get events links
    event_links = []
    # find the table with the events
    events_table = soup.find("table", {"class": "view-calendar-list"})

    # loop through the rows and extract the links
    for row in events_table.find_all("tr"):
        link = row.find("a")
        if link:
            main = 'https://religiousstudies.yale.edu'
            event_links.append(main + link["href"])

    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('title').text.strip()

        # speaker
        speaker_name = None
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

            address = soup.find('span', {'class': 'fn'}).text.strip()

        except:
            address = "TBD"

        try:
            desc_tag = soup.find('div', {'class': 'field-type-text-with-summary'})
            description = ""
            for p in desc_tag.find_all('p'):
                description += p.text.strip() + " "
        except:
            description = None

        print(description)
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
            "description": description,
            "link": link
        }
        return event

    # get all events for African american department
    events = []
    for link in event_links:
        event = get_event(link)
        events.append(event)
    return events





department_parsers = {
"https://religiousstudies.yale.edu/": Renaissance_Studies

}

def get_all_events_R():
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
