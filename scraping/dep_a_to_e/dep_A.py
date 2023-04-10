"""
This is script for getting all the events for departments starting with letter A
"""
import requests
from bs4 import BeautifulSoup
import sys
from DateTime import getDate, getTime
from dep_events import all_department_links, get_dep_events
import json
import re
from datetime import datetime


##-------------------African American Dep---------------##
def african_american_studies(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")

    # get events links
    event_links = []
    for row in soup.select("table.view-calendar-list tr"):
        link = row.select_one("a[href^='/event/']")
        if link:
            event_links.append(link["href"])

    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('h1', {'id': 'page-title'}).text.strip()

        # speaker
        name_div = soup.find('div', {'class': 'field-name-field-speaker-name'})
        speaker_name = name_div.find('div', {'class': 'field-item even'}).text.strip()

        # speaker title
        speaker_div = soup.find('div', {'class': 'field-name-field-speaker-title'})
        speaker_title = speaker_div.find('div', {'class': 'field-item even'}).text.strip()

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

        # getting location
        map_icon = soup.select_one('span.map-icon')
        map_icon.extract()
        location_div = soup.find('div', class_='field-name-field-location')
        location_spans = [span.text.strip() for span in location_div.find_all('span') if span.get('class') != ['map-icon']]
        address = ', '.join(location_spans)

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
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


##---------------African Studies--------------##

def african_studies(main_url, calendar, dep):
    """Afrian studies dep"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")

    # get events links
    event_links = []
    for row in soup.select("table.view-calendar-list tr"):
        link = row.select_one("a[href^='/event/']")
        if link:
            event_links.append(link["href"])

    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('h1', {'id': 'page-title'}).text.strip()

        # speaker
        name_div = soup.find('div', {'class': 'field-name-field-speaker-performer'})
        speaker_name = name_div.find('div', {'class': 'field-item even'}).text.strip()

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
        # getting location
        # Remove the span with class 'map-icon'
        map_icon = soup.select_one('span.map-icon')
        map_icon.extract()
        location_div = soup.find('div', class_='field-name-field-location')
        location_spans = [span.text.strip() for span in location_div.find_all('span') if span.get('class') != ['map-icon']]
        address = ', '.join(location_spans)

        # description
        desc_tag = soup.find('div', class_='field-type-text-with-summary')
        description = desc_tag.find('div', class_='field-item even').find_next('p').text.strip()

         # Event object as a dictionary
        event = {
            "title": title,
            "speaker": speaker_name,
            "department": dep,
            "date": date,
            "time": time,
            "location": address,
            "description": description,
            "iso_date": iso,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events

#####---------------American Studies------------------------########
def american_studies(main_url, calendar, dep):
    """A function that returns american studies events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")

    # get events links
    # Find the table with the specified class
    table = soup.find('table', class_='view-calendar-list')

    # Extract all the links within the table
    try:
        links = [a['href'] for a in table.find_all('a')]
    except:
        links = []

    def get_event(link):
        """Getting events"""
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        # title
        title = soup.find('h1', {'id': 'page-title'}).text.strip()

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
        # getting location
        # Find the location div
        location_div = soup.find('div', class_='location')
        # Extract the fn and street-address content
        fn = location_div.find('span', class_='fn').text.strip()
        street_address = location_div.find('div', class_='street-address').text.strip()
        # Combine the fn and street-address content into a single string
        address = f"{fn}, {street_address}"

         # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
        }
        return event
    # get all events
    events = get_dep_events(main_url, get_event, links)
    return events

####------------------Anthropology-----------------------####
def anthropology(main_url, calendar, dep):
    """Anthropology department"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    
    
    # get events links
    links = []
    for row in soup.select("table.view-calendar-list tr"):
        link = row.select_one("a[href^='/event/']")
        if link:
            links.append(link["href"])
    

    def get_event(link):
        """Get event details"""
        page = requests.get(link)
    
        soup = BeautifulSoup(page.content, "html.parser")
        # title
        title = soup.find('h1', {'id': 'page-title'}).text.strip()
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
        # Find the location div
        location_div = soup.find('div', class_='location')
        # Extract the fn and street-address content
        address = None
        fn = location_div.find('span', class_='fn')
        if fn:
            address = fn.text.strip()
        # street address
        street = location_div.find('div', class_='street-address')
        if street:
            address = street.text.strip()

        # searching for event description
        description = None
        desc_tag = soup.find('div', class_='field-type-text-with-summary')
        if desc_tag:
            p_tags = desc_tag.find_all('p')
            description = '\n'.join(p.get_text(strip=True) for p in p_tags)

        speaker = None
        if title.split(":")[1].strip():
            speaker = title.split(":")[1].strip()

        # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker":speaker,
            "date": date,
            "time": time,
            "location": address,
            "description": description,
            "iso_date": iso,
        }
        return event
    # get all events
    events = get_dep_events(main_url, get_event, links)
    return events

####------------------anesthesiology-----------------------####
def anesthesiology(main_url, calendar, dep):
    """anesthesiology department"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")

    links = []
    all_links = soup.find_all('div', class_='event-list-item__details')
    for event in all_links:
        link = event.find('a')['href']
        new_link = 'https://medicine.yale.edu' + link
        links.append(new_link)
 
    
    def get_event(link):
        """Get event details"""
        page = requests.get(link)
        
        soup = BeautifulSoup(page.content, "html.parser")
        
        # title
        try:
            title = soup.find("h1", class_="event-details-header__title").text.strip()
        except:
            title = ""

        
        try:
            date_year = soup.find("span", class_="event-date__month-year").text.split()
            date_month = date_year[0]
            date_year = date_year[1]
        except AttributeError:
            date_month = ""
            date_year = ""
        date_day = soup.find("span", class_="event-date__day").text.strip()
        date = f"{date_month}/{date_day}/{date_year}"

        try:
            date_start_time = soup.find("span", class_="event-time__start-date").text.split()[0]
        except AttributeError:
            date_start_time = ""

        # date_end_time = soup.find("span", class_="event-time__end-date").text.strip()

        try:
            speaker = soup.find("span", class_="profile-detailed-info-list-item__name").text.strip()
        except AttributeError:
            speaker = ""

        try:
            description = soup.find("div", class_="event-details-info__description").text.strip()
        except AttributeError:
            description = ""

        try:
            address = soup.find("span", class_="link__label").text.strip()
        except AttributeError:
            address = ""

        
        event = {
            "title": title,
            "department": dep,
            "speaker":speaker,
            "date": date,
            "time": date_start_time[0],
            "location": address,
            "description": description,
            "iso_date": None,
        }
        return event
    # get all events
    events = get_dep_events(main_url, get_event, links)
    return events

####------------------Applied_Mathematics-----------------------####
def applied_mathematics(main_url, calendar, dep):

        # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
        # get events links
    links = []
    for row in soup.select("table.view-calendar-list tr"):
        link = row.select_one("a[href^='/event/']")
        if link:
            links.append(link["href"])
   
    def get_event(link):
        """Get event details"""
        page = requests.get(link)
    
        soup = BeautifulSoup(page.content, "html.parser")
        # title
        title = soup.find('h1', {'id': 'page-title'}).text.strip()
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
        # Find the location div
        location_div = soup.find('div', class_='location')
        # Extract the fn and street-address content
        address = None
        fn = location_div.find('span', class_='fn')
        if fn:
            address = fn.text.strip()
        # street address
        street = location_div.find('div', class_='street-address')
        if street:
            address = street.text.strip()

        # searching for event description
        description = None
        desc_tag = soup.find('div', class_='field-type-text-with-summary')
        if desc_tag:
            p_tags = desc_tag.find_all('p')
            description = '\n'.join(p.get_text(strip=True) for p in p_tags)

        try:
            speaker = soup.find("div", class_="field-item even").text.strip()
        except AttributeError:
            speaker = ""

        # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker":speaker,
            "date": date,
            "time": time,
            "location": address,
            "description": description,
            "iso_date": iso,
        }
        return event
    # get all events
    events = get_dep_events(main_url, get_event, links)
    return events

####------------------Applied_Mathematics-----------------------####
def Applied_Physics(main_url, calendar, dep):

        # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
      # get events links
    links = []
    try:
        for row in soup.select("table.view-calendar-list tr"):
            link = row.select_one("a[href^='/event/']")
            if link:
                links.append(link["href"])
    except:
        links = []
    
    def get_event(link):
        """Get event details"""
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('h1', {'id': 'page-title'}).text.strip()
        # time and date
        

        try:
            date_div = soup.find('div', {'class': 'field-name-field-event-time'})
            date_str = date_div.find('span', {'class': 'date-display-single'})
        except:
            date_div = None
            date_str = None

        if date_str.has_attr('content'):
            content_attr = date_str['content']
            iso = content_attr
            date = getDate(content_attr)
            time = getTime(content_attr)
        else:
            date_str = soup.find('h4', text=lambda t: "Date" in t)
            content_attr = date_str['content']
            iso = content_attr
            date = getDate(content_attr)
            time = getTime(content_attr)
        # Find the location div

        # try: 
        location_tag = soup.find('h4', string=lambda s: s and 'Location:' in s)
        if location_tag:
            address  = location_tag.text.split('Location:', 1)[1].strip()
        else:
            address = 'TBD'
            
        description = None
        
        speaker = None

        # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker":speaker,
            "date": date,
            "time": time,
            "location": address,
            "description": description,
            "iso_date": iso,
        }
        return event
    # get all events
    events = get_dep_events(main_url, get_event, links)
    return events


##-------------------Architecture Studies Dep---------------##
def Architecture(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    
    event_links = []

    all_links = soup.find_all("a", {"class": "hover-link-row", "data-modal-title": "Lectures"})
    
    for event in all_links:
        link = event["href"]
        event_links.append(link)
   
    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        # title
        title = soup.find('title').text.strip()
        # speaker
        speaker_name = soup.find('span', {'class': 'event__speaker-names'}).text.strip()

        # speaker title
        speaker_title = None
        iso = None
        address = None
        # time and date
        date_str = None

        date_str = soup.find('h2', {'class': 'event__metadata-title h2'}).text.strip()
        address = soup.find_all('h2', {'class': 'event__metadata-title h2'})[1].text.strip()
        date_format = '%A, %B %d, %Y %I:%M %p'

        try:
            iso = datetime.strptime(date_str, date_format).isoformat()
            
        except:
            iso = None
            date = date_str
            time = date_str
        
        if iso:
            date = getDate(iso)
            time = getTime(iso)
        else:
            date = None
            time = None

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": speaker_title,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


##-------------------Astronomy Dep---------------##
def Astronomy(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    # get events links
    event_links = []
    events = soup.find_all('div', class_="views-field views-field-title")
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

        address = soup.find('span', {'class': 'fn'}).text.strip()

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
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events



####---------------Get ALL Events for departments starting with letter A------####
# A dictionary of department links and functions to get events
department_parsers = {
    "https://african.macmillan.yale.edu/": african_studies,
    "https://afamstudies.yale.edu/": african_american_studies,
    "https://americanstudies.yale.edu/": american_studies,
    "https://anthropology.yale.edu/": anthropology,
    "https://medicine.yale.edu/anesthesiology/": anesthesiology,
    "https://applied.math.yale.edu/": applied_mathematics,
    "https://appliedphysics.yale.edu/": Applied_Physics,
    "https://www.architecture.yale.edu/": Architecture,
    "https://astronomy.yale.edu/": Astronomy


}

def get_all_events_A():
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

if __name__ == "__main__":
    events = get_all_events_A()
    print(events)








