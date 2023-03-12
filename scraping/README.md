__# Web Scraping Events__
----------------------
----------------------
This folder contains Python scripts that are intended for scraping events from different websites. The scripts use requests and BeautifulSoup libraries for sending HTTP requests and parsing HTML pages.

**## Requirements**
⋅⋅* Python 3.x
⋅⋅* requests library
⋅⋅* BeautifulSoup library

**## How it Works**
Note that different websites have different html structure, therefore, there is the need to create a webscraping script for each individual website.

For each script, there is a function:

### get_(department)_events()

upon calling the above function, it will scrape the upcoming events of the selected department. The function returns a list of events, with each event as a dictionary of different parts of the events:

#### Example

calling the function *get_cs_events()* will return a list of the cs_department upcoming events as a list, each item in the list will contain an event as a dictionary
The keys will be:
* type -> type of event
* title -> title of event
* speaker -> the speaker of the event
* host -> host of the event
* date
* time -> time in EST, In the script there is a function **getTime(str)** which converts the time to EST
* location
* abstract -> The abstract of the event
* bio -> bio of the speaker of the event

**##How to Use**
To use functions in another file in another python file in the applictaion, you need to import the function that you need to use.
###Example
* If you want to use the function that gets events from cs department in the *databaseConfig.py* file, you need to import the function as shown:
```python
from scraping.cs_dept_events import get_cs_events

# List of events
events = get_cs_events()

```

**##Disclaimer##**
The downside of webscraping is that the scripts may sometimes fail if the owners of websites decide to change the structure of their websites. Therefore, we need to regularly confime if the scripts actually get any data from the websites.