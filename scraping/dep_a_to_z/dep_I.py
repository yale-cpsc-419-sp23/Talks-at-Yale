"""
This is script for getting all the events for departments starting with letter C
"""
import requests
from bs4 import BeautifulSoup
from dep_events import all_department_links, get_dep_events
import json
from DateTime import getDate, getTime

def International_Development_Economics(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("li",{"class": "menu__item"})

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
            speaker_name = soup.find('p').text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        try:
            time = soup.find('div',{'class':'node__event-time'}).text.strip()
           
            
        except:
            time = "TBD"
        # we get the date of the event
        try:
            date = soup.find('div',{'class': 'ode__event-date'}).text.strip()

        except:
            date = "TBD"
        # we get the address 
        try:
            address = soup.find('div',{'class': 'ode__address-label'}).text.strip()
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
            "link": link,
        }
        return event
    
    events = get_dep_events(main_url, get_event, event_links)
    return events


def italian(main_url, calendar, dep):
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
        try:

            speaker_name = soup.find('div', {'class': 'field-name-field-speaker'}).text.split(':')[-1].strip()
        except:
            speaker_name = "TBD"
        try:
            # time and date
            date_div = soup.find('div', {'class': 'field-name-field-event-time'})
            date_str = soup.find('span', {'class': 'date-display-single'})

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
"https://economics.yale.edu/ide-ma-program": "International_Development_Economics",
"https://italian.yale.edu/": italian
}

def get_all_events_C():
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
