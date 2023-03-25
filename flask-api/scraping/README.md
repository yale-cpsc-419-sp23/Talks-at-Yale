# Web Scraping Events
----------------------
----------------------
This folder contains Python scripts that are intended for scraping events from different websites. The scripts use requests and BeautifulSoup libraries for sending HTTP requests and parsing HTML pages.

## Requirements
* Python 3.x
* requests library
* BeautifulSoup library

## How it Works
The scraping folder is modularized, in a way that scraping department events is separated into different folders,
#### Example
departments starting with letter a to e are in folder *dep_a_to_e*

There is a file main.py which has function *all_events*, import this function and call it to get all events, this events will only be upcoming events

#### Example Usage

``` python
# Import
from scraping.main import all_events

# call function
events = all_events()

```
the return value will be a list of dictionary. Each dictionary representing an event. For example, all cs department events will have the following format
The keys will be:
* type -> type of event
* title -> title of event
* speaker -> the speaker of the event
* host -> host of the event
* date
* time -> time in EST, In the script there is a function *getTime(str)* which converts the time to EST
* location
* abstract -> The abstract of the event
* bio -> bio of the speaker of the event

## Disclaimer
The downside of webscraping is that the scripts may sometimes fail if the owners of websites decide to change the structure of their websites. Therefore, we need to regularly confime if the scripts actually get any data from the websites.