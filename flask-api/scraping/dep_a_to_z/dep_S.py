
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


def Statistics_Data_Science(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    links_div =soup.find("div",{"class": "view-calendar-list"})
    all_links = links_div.find_all()
    try:
        for div in all_links:
            link = div.find('a').get('href').split('/neuroscience')[1]
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

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": "TBD",
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events

def Spanish_Portuguese(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
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

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": "TBD",
            "link": link,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
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
