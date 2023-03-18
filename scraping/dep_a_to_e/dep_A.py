"""
This is script for getting all the events for departments starting with letter A
"""
import requests
from bs4 import BeautifulSoup
import sys
from scraping.DateTime import getDate, getTime
from scraping.dep_events import all_department_links, get_dep_events

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
    links = [a['href'] for a in table.find_all('a')]

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



####---------------Get ALL Events for departments starting with letter A------####
# A dictionary of department links and functions to get events
department_parsers = {
    "https://african.macmillan.yale.edu/": african_studies,
    "https://afamstudies.yale.edu/": african_american_studies,
    "https://americanstudies.yale.edu/": american_studies,
    "https://anthropology.yale.edu/": anthropology,

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








