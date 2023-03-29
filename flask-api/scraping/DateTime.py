"""Helper functions to be used in formating the data scrapped from departments"""
from datetime import datetime

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