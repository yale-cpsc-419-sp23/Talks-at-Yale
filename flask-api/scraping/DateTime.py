"""Helper functions to be used in formating the data scrapped from departments"""
from datetime import datetime
from dateutil import parser

###-------------- Functions ------------------------------###

def getDate(str):
    """Gets date in the format year/month/date from a string of date"""
    date_time_obj = datetime.fromisoformat(str)
    # Get the date components
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    return f"{year}/{month}/{day}"

def getTime(str):
    """Gets time in 24 hour clock EST from a string of date"""
    date_time_obj = datetime.fromisoformat(str)
    # Get the time components
    hour = date_time_obj.hour
    minute = date_time_obj.minute
    return date_time_obj.strftime("%H:%M")

import datetime

def getISO(date_str):
    """Convert date to ISO format"""
    # parse the input date string using dateutil
    date = parser.parse(date_str)
    # format the datetime object in ISO format
    iso_date = date.strftime("%Y-%m-%dT%H:%M:%S")
    return iso_date

# input date string in various formats
date_str1 = "Monday, June 28 2005"
date_str2 = "April 4 2024"
date_str3 = "28/05/2023"

# call the function to get the date in ISO format
result1 = getISO(date_str1)
result2 = getISO(date_str2)
result3 = getISO(date_str3)

# output the ISO-formatted dates
print(result1)
print(result2)
print(result3)