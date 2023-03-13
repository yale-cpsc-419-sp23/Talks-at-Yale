import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Website url
main_url = "https://cpsc.yale.edu"
calendar_url = "/calendar"


# send request to the url
response = requests.get(main_url + calendar_url)
soup = BeautifulSoup(response.content, "html.parser")

# get event links
event_links = soup.select('td.views-field-title > a')


###-------------- Functions ------------------------------###

def getDate(str):
    """Gets date in the format year/month/date from a string of date"""
    date_obj = datetime.strptime(str, "%A, %B %d, %Y - %I:%M%p")
    year = date_obj.strftime("%Y")
    month = date_obj.strftime("%m")
    day = date_obj.strftime("%d")

    clean_date = f"{year}/{month}/{day}"
    return clean_date

def getTime(str):
    """Gets time in 24 hour clock EST from a string of date"""
    date_obj = datetime.strptime(str, "%A, %B %d, %Y - %I:%M%p")
    hour = date_obj.strftime("%H")
    minute = date_obj.strftime("%M")

    clean_time = f"{hour}:{minute}"
    return clean_time

def getEventDetails(event_link):
    """Returns event details given a link of page"""
    event_response = requests.get(event_link)
    event_soup = BeautifulSoup(event_response.content, 'html.parser')

    # Extract relevant data from html page

    # Getting event type
    type_tag = event_soup.find('h1', {'id': 'page-title'})
    type = type_tag.text.strip()

    # Getting location
    room_tag = event_soup.find('span', {'class': 'fn'})
    room = room_tag.text.strip()
    street_tag = event_soup.find('div', {'class': 'street-address'})
    street = street_tag.text.strip()
    city_tag = event_soup.find('span', {'class': 'locality'})
    city = city_tag.text.strip()
    state_tag = event_soup.find('span', {'class': 'region'})
    state = state_tag.text.strip()
    code_tag = event_soup.find('span', {'class': 'postal-code'})
    code = code_tag.text.strip()

    # location
    location = ", ".join([room, street, city, state, code])


    # Find the div tag with necessay info such as title, host
    info_tag = event_soup.find('div', {'property': 'content:encoded'})

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

    # getting the date
    date_tag = event_soup.find('span', {'class': 'date-display-single'})
    date_str = date_tag.text.strip()

    date = getDate(date_str)
    time = getTime(date_str)

    # Event object as a dictionary
    event = {
        "type": type,
        "title": title,
        "speaker": speaker_name,
        "host": host,
        "date": date,
        "time": time,
        "location": location,
        "abstract": abstract,
        "bio": bio,
    }
    return event


def get_cs_events():
    """A function that returns all events in the CS department website"""
    all_events = []
    for link in event_links:
        event_url = main_url + link['href']
        event  = getEventDetails(event_url)
        all_events.append(event)
    return all_events
