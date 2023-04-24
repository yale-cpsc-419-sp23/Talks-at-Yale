
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


def Statistics_Data_Science(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'calendar/year')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # find the table with the events
    events_table = soup.find("table", {"class": "views-view-grid"})

    # loop through the rows and extract the links
    for row in events_table.find_all("tr"):
        link = row.find("a")
        if link:
            main = 'https://statistics.yale.edu'
            event_links.append(main + link["href"])

    # A function that goes to each link and gets the events details
    def get_event(link):

        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        try:
            title = soup.find('div', {'class': 'field-name-field-abstract-title'}).text.strip()
        except:
            title = "TBD"

            # speaker
        try:
            speaker_name = soup.find('h1', {'class':'title'}).text.strip()
        except:
            speaker_name = "TBD"

        # time and date
        iso = None
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
        # we get the address
        try:
            address = soup.find('span',{'class': 'fn'}).text.strip()
        except:
            address = "TBD"
        try:
            desc_tag = soup.find('div', {'class': 'field-type-text-with-summary'})
            description = desc_tag.find('div', {'class':'field-items'}).text.strip()
        except:
            description = None

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "description": description,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link,
            "iso": iso,
        }
        return event

    # get all events for African american department
    events = []
    for link in event_links:
        event = get_event(link)
        events.append(event)
    return events

def Spanish_Portuguese(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'calendar/month')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # find the table with the events
    events_table = soup.find("table", {"class": "view-calendar-list"})

    # loop through the rows and extract the links
    for row in events_table.find_all("tr"):
        link = row.find("a")
        if link:
            main = 'https://span-port.yale.edu'
            event_links.append(main + link["href"])

    # A function that goes to each link and gets the events details
    def get_event(link):

        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

       # title
        try:
            title = soup.find('h1',{'class':'title'}).text.strip()
        except:
            title = "TBD"

            # speaker
        try:
            speaker_name = soup.find('h1', {'id':'page-title'}).text.strip()
        except:
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
        # we get the address
        try:
            address = soup.find('span',{'class': 'fn'}).text.strip()


        except:
            address = "TBD"

        try:
            desc_tag = soup.find('div', {'class': 'field-type-text-with-summary'})
            description = ""
            for p in desc_tag.find_all('p'):
                description += p.text.strip() + " "
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
            "description": description,
            "iso_date": iso,
            "link": link,
        }
        return event

    # get all events for African american department
    events = []
    for link in event_links:
        event = get_event(link)
        events.append(event)
    return events



department_parsers = {
"https://statistics.yale.edu/": Statistics_Data_Science,
"https://span-port.yale.edu/": Spanish_Portuguese

}

def get_all_events_S():
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
