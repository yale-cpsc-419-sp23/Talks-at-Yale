"""
This is script for getting all the events for departments starting with letter C
"""
import requests
from bs4 import BeautifulSoup
from DateTime import getDate, getTime
from dep_events import all_department_links, get_dep_events


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

        # Event object as a dictionary
        event = {
            "type": type,
            "title": title,
            "speaker": speaker_name,
            "host": host,
            "date": date,
            "time": time,
            "iso_date": iso,
            "location": location,
            "description": abstract,
            "bio": bio,
        }
        return event
    # get all events for cs dep
    main_url = ""
    events = get_dep_events(main_url, get_event, event_links)
    return events

## --------Cell Biology-----###





##---All department events starting with letter c----##

department_parsers = {
    "https://cpsc.yale.edu/": computer_science,
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

