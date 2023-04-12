"""
This is script for getting all the events for departments starting with letter C
"""
import requests
from bs4 import BeautifulSoup
from dep_events import all_department_links, get_dep_events
import json
from DateTime import getDate, getTime



###---------------CS Department-----------------------####
def computer_science(main_url, calendar, dep):
    """Getting CS department events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")

    # get events link
    event_links = []
    links_tag = soup.select('td.views-field-title > a')
    for link in links_tag:
        event_url = main_url + link['href']
        event_links.append(event_url)

    def get_event(link):
        """A function that gets event given a link"""
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # Getting event type
        type = soup.find('h1', {'id': 'page-title'}).text.strip()

        # Getting location
        room = soup.find('span', {'class': 'fn'}).text.strip()
        street = soup.find('div', {'class': 'street-address'}).text.strip()
        city = soup.find('span', {'class': 'locality'}).text.strip()
        state = soup.find('span', {'class': 'region'}).text.strip()
        code = soup.find('span', {'class': 'postal-code'}).text.strip()
        # location
        location = ", ".join([room, street, city, state, code])

        # Find the div tag with necessay info such as title, host
        info_tag = soup.find('div', {'property': 'content:encoded'})
        # speaker
        speaker_p = info_tag.find('p')
        speaker_name = speaker_p.contents[-1].strip()
        # Initialize the info we are looking for to None
        host = title = abstract = bio = None

        if info_tag:
            for p in info_tag.find_all('p'):
                text = p.get_text().strip()
                if text.startswith('Host:'):
                    host = text.replace('Host:', '').strip()
                elif text.startswith('Title:'):
                    title = text.replace('Title:', '').strip()
                elif text.startswith('Abstract:'):
                    abstract = p.find_next('p').get_text().strip()
                elif text.startswith('Bio:'):
                    bio = p.find_next('p').get_text().strip()

        # getting time
        date_tag = soup.find('span', {'class': 'date-display-single'})
        if date_tag.has_attr('content'):
            content_attr = date_tag['content']
            iso = content_attr
            date = getDate(content_attr)
            time = getTime(content_attr)

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": None,
            "iso_date": iso,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events

def Cell_Biology(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split('/cellbio')[1]
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
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events
def Cellular_Molecular_Physiology(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split('physiology/')[1]
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
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Chemical_Environmental_Engineering(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'news-events/events?type=All&tid_1=2&keys=')
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
            address = ""
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

def Chemistry(main_url, calendar, dep):
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
            location = None
            for p in soup.find_all('p'):
                if 'Location:' in p.text:
                    location = p.text.split(':')[1].strip()
                    break
            address = location

            if location is None:
                address = "TBD"
            else:
                if 'Time' in location.text:
                    address = "TBD"
                else:
                    address = location
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
##---All department events starting with letter c----##

def child_Study_Center(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + '/news/calendar/')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split('/childstudy')[1]
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
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events

def Chronic_Disease_Epidemiology(main_url, calendar, dep):
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
    
         # Event object as a dictionary
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

def classics(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("td",{"class": "views-field views-field-title-1"})

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
            location = None
            for p in soup.find_all('p'):
                if 'Location:' in p.text:
                    location = p.text.split(':')[1].strip()
                    break
            address = location

            if location is None:
                address = "TBD"
            else:
                if 'Time' in location.text:
                    address = "TBD"
                else:
                    address = location
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
def Cognitive_Science(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + '/events')
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
    
         # Event object as a dictionary
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

def Comparative_Literature(main_url, calendar, dep):
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
            location = None
            for p in soup.find_all('p'):
                if 'Location:' in p.text:
                    location = p.text.split(':')[1].strip()
                    break
            address = location

            if location is None:
                address = "TBD"
            else:
                if 'Time' in location.text:
                    address = "TBD"
                else:
                    address = location
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


def Comparative_Medicine(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []
    
    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split('compmed/')[1]
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
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Computational_Biology_Bioinformatics(main_url, calendar, dep):
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
            speaker_name = soup.find('p').text.strip()
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



department_parsers = {
    "https://cpsc.yale.edu/": computer_science,
    "https://medicine.yale.edu/cellbio/": Cell_Biology,
    "https://medicine.yale.edu/physiology/": Cellular_Molecular_Physiology,
    "https://seas.yale.edu/": Chemical_Environmental_Engineering,
    "https://chem.yale.edu/": Chemistry,
    "https://medicine.yale.edu/childstudy/": child_Study_Center,
    "https://ysph.yale.edu/": Chronic_Disease_Epidemiology,
    "https://classics.yale.edu/": classics,
    "https://cogsci.yale.edu/": Cognitive_Science,
    "https://complit.yale.edu/": Comparative_Literature,
    "https://medicine.yale.edu/compmed/": Comparative_Medicine,
    "https://cbb.yale.edu/": Computational_Biology_Bioinformatics
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

