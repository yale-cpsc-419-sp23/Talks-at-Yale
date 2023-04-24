"""
A python script that gets events from all the departments at Yale Universtiy.
"""
import requests
from bs4 import BeautifulSoup
# Yale department program url
main_url = "https://www.yale.edu/academics/departments-programs"

# send request to the url
response = requests.get(main_url)
soup = BeautifulSoup(response.content, "html.parser")

# find the names of the dapartments and their website links in the html page
# We will store the names of the dapartments as keys while the links will be the value
def all_department_links():
    """A function that returns all departments links"""
    departments_dict = {}
    for article in soup.select('article.department_item'):
        # get the department name
        department_name = article.find('a', class_ = 'department_item_link').text
        # get the department link
        department_link = article.find('a', class_='department_item_link')['href']
        # put into the dictionary
        departments_dict[department_name] = department_link
    return departments_dict


def get_dep_events(main_link, func, links):
    """Gets events for a particular department given a function, and a list of event links"""
    events = []
    for link in links:
        event = func(main_link+link)
        events.append(event)
    return events
