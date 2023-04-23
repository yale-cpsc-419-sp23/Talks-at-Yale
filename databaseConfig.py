import sqlite3
import os
from scraping.main import all_events


def searchEventsDatabase(searchTerm=None):
    """returns the database object. If searchterm is empty, it will return the full database, otherwise If a search term is provided, it will return the search results instead.

    Args:
        searchTerm (str): the search term to search the database for."""


    # print(searchTerm)
    c = sqlite3.connect('events.db')

    # we now print the entire database
    # print(c.execute("SELECT * FROM events").fetchall())

    # default behavior is to return the full database if the search term is empty
    if searchTerm is None:
        events = c.execute("SELECT * FROM events")
        return events

    # if a search term is provided, it will return the search results instead
    query = """SELECT *
        FROM events
        LEFT JOIN speakers ON events.speaker_id = speakers.id
        LEFT JOIN hosts ON events.host_id = hosts.id
        WHERE title LIKE :searchTerm OR speaker_name LIKE :searchTerm OR host_name LIKE :searchTerm"""
    events = c.execute(query, {"searchTerm": f'%{searchTerm}%'})
    # print(events.fetchall())
    return events.fetchall()

def addFavorite(user_id, event_id):
    """adds an event to the user's favorites list."""
    c = sqlite3.connect('events.db')
    c.execute("INSERT INTO user_events (user_id, event_id) VALUES (?, ?)", (user_id, event_id))
    c.commit()
    c.close()

def removeFavorite(user_id, event_id):
    """removes an event from the user's favorites list."""
    c = sqlite3.connect('events.db')
    c.execute("DELETE FROM user_events WHERE user_id = ? AND event_id = ?", (user_id, event_id))
    c.commit()
    c.close()

def searchUserFavorites(user_id):
    """returns the user's favorite events."""
    c = sqlite3.connect('events.db')
    events = c.execute("SELECT * FROM user_events WHERE user_id = ?", (user_id,)).fetchall()
    c.close()
    return events

def createDatabase():
    # Connect to a database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('events.db')

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Create the tables

    c.execute('''CREATE TABLE types(
                id INTEGER,
                type TEXT UNIQUE,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE speakers(
                id INTEGER,
                speaker_name TEXT UNIQUE,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE hosts(
                id INTEGER,
                host_name TEXT UNIQUE,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE locations(
                id INTEGER,
                location TEXT UNIQUE,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE departments(
                id INTEGER,
                department TEXT UNIQUE,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE events(
                id INTEGER,
                type_id INTEGER,
                title TEXT,
                speaker_id INTEGER,
                host_id INTEGER,
                date TEXT,
                iso_date TEXT,
                time TEXT,
                location_id INTEGER,
                bio, TEXT,
                info TEXT,
                department_id INTEGER,
                FOREIGN KEY (type_id) REFERENCES types(id),
                FOREIGN KEY (speaker_id) REFERENCES speakers(id),
                FOREIGN KEY (host_id) REFERENCES hosts(id),
                FOREIGN KEY (location_id) REFERENCES locations(id),
                FOREIGN KEY (department_id) REFERENCES departments(id),
                PRIMARY KEY (id, department_id, type_id, speaker_id, host_id, location_id))''')

    c.execute('''CREATE TABLE users(
                user_id INTEGER,
                PRIMARY KEY (user_id))''')

    c.execute('''CREATE TABLE user_events(
                user_id INTEGER,
                event_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (event_id) REFERENCES events(id))''')

    # Save (commit) the changes, and then close the connection
    conn.commit()
    conn.close()

def populateDatabase(verbose=False):
    """adds events to the events database.
        events are pulled from the department website, through the use of the web scraper."""

    conn = sqlite3.connect('events.db')
    c = conn.cursor()

    # get all events from the web scraper
    events = all_events()

    for event in events:

        # get the event data from the passed in dict
        title = event.get('title')
        department = event.get('department')
        event_type = event.get('type')
        speaker = event.get('speaker')
        speaker_title = event.get('speaker_title')
        host = event.get('host')
        date = event.get('date')
        time = event.get('time')
        location = event.get('location')
        iso_date = event.get('iso_date')
        bio = event.get('bio')

        # add the type to the types table, and get the type id
        if event_type is None:
            event_type = "N/A"
        c.execute("INSERT OR IGNORE INTO types (type) VALUES (?)", (event_type,))
        type_id = c.execute("SELECT id FROM types WHERE type = ?", (event_type,)).fetchone()[0]

        # add the speaker to the speakers table, and get the speaker id
        # if speaker_title:                                 # can be implemented later, but adds a lot of extra words to the speaker name
        #     speaker = speaker + ", " + speaker_title
        if speaker is None:
            speaker = "N/A"
        c.execute("INSERT OR IGNORE INTO speakers (speaker_name) VALUES (?)", (speaker,))
        speaker_id = c.execute("SELECT id FROM speakers WHERE speaker_name = ?", (speaker,)).fetchone()[0]

        # add the host to the hosts table, and get the host id
        if host is None:
            host = "N/A"
        c.execute("INSERT OR IGNORE INTO hosts (host_name) VALUES (?)", (host,))
        host_id = c.execute("SELECT id FROM hosts WHERE host_name = ?", (host,)).fetchone()[0]

        # add the location to the locations table, and get the location id
        if location is None:
            location = "N/A"
        c.execute("INSERT OR IGNORE INTO locations (location) VALUES (?)", (location,))
        location_id = c.execute("SELECT id FROM locations WHERE location = ?", (location,)).fetchone()[0]

        # add the department to the departments table, and get the department id
        if department is None:
            department = "N/A"
        c.execute("INSERT OR IGNORE INTO departments (department) VALUES (?)", (department,))
        department_id = c.execute("SELECT id FROM departments WHERE department = ?", (department,)).fetchone()[0]

        # add the event to the events table
        # we make the assumption that the events being passed in are unique
        if title is None:
            title = "N/A"
        if date is None:
            date = "N/A"
        if iso_date is None:
            iso_date = "N/A"
        if time is None:
            time = "N/A"
        if bio is None:
            bio = "N/A"
        c.execute("INSERT INTO events (type_id, title, speaker_id, host_id, date, iso_date, time, location_id, bio, department_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (type_id, title, speaker_id, host_id, date, iso_date, time, location_id, bio, department_id))

        # print the databases if verbose is true
    if verbose:
        print("\nverbose mode in populateDatabase():\n")

        print("types:\n")
        test = c.execute("SELECT * FROM types")
        print(test.fetchall())

        print("speakers:\n")
        test = c.execute("SELECT * FROM speakers")
        print(test.fetchall())

        print("hosts:\n")
        test = c.execute("SELECT * FROM hosts")
        print(test.fetchall())

        print("locations:\n")
        test = c.execute("SELECT * FROM locations")
        print(test.fetchall())

        print("departments:\n")
        test = c.execute("SELECT * FROM departments")
        print(test.fetchall())

        print("events:\n")
        test = c.execute("SELECT * FROM events")
        print(test.fetchall())


    # Save (commit) the changes, and then close the connection
    conn.commit()
    conn.close()


def populateDatabaseOld(verbose=False):
    """adds preformatted events to the created database.

        THIS IS AN OLD VERSION OF THE DATABASE POPULATOR. USE populateDatabase() INSTEAD.
        This function is kept for reference purposes, and will be removed in the future."""

    # Connect to a database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('events.db')
    c = conn.cursor()

    # populates the types table
    types = ['CS Talk - Faculty Recruit', 'Dissertation Defense', 'EE Seminar', 'other']
    for i in range(len(types)):
        c.execute("INSERT INTO types (type, id) VALUES (?, ?)", (types[i], i))

    # populates the speakers table
    speakers = ['Jay Lim', 'Jialu Zhang', 'Dr. Shuwen Deng', 'Aldo Pacchiano', 'Jake Brawer', 'Wenjie Xiong', 'Talley Amir', 'Weijie Su', 'NA']
    for i in range(len(speakers)):
        c.execute("INSERT INTO speakers (speaker_name, id) VALUES (?, ?)", (speakers[i], i))

    # populates the hosts table
    hosts = ['Ruzica Piskac', 'Professor Jakub Szefer', 'Steve Zucker', 'Brian Scassellati', 'Jakub Szefer', 'James Aspnes', 'NA']
    for i in range(len(hosts)):
        c.execute("INSERT INTO hosts (host_name, id) VALUES (?, ?)", (hosts[i], i))

    # populates the locations table
    locations = ['AWK 200', 'AKW 307', 'LC 105', 'AKW 200, 51 Prospect Street', 'TBD', '87 Trumbull St, Room B120', 'NA']
    for i in range(len(locations)):
        c.execute("INSERT INTO locations (location, id) VALUES (?, ?)", (locations[i], i))

    # populates the departments table
    departments = ['Computer Science']
    for i in range(len(departments)):
        c.execute("INSERT INTO departments (department, id) VALUES (?, ?)", (departments[i], i))

    # populates the events table
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (0, 0, 'CS Talk - Faculty Recruit', 'Jay Lim', 0, 'Tuesday, February 28', '4:00 p.m.', 0, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (1, 1, 'Automatically Preventing, Detecting, and Repairing Crucial Errors in Programs', 1, 0, 'March 6th, 2023', '1 PM EST.', 1, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (2, 2, 'NA', 2, 2, 'Thursday, March 9, 2023', '10:00 AM.', 6, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (3, 3, 'Robot Abuse: Is it okay for me to hit my robot?', 8, 6, 'February 28', '5:00 p.m.', 2, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (4, 0, 'Learning Systems in Adaptive Environments. Theory, Algorithms and Design', 3, 2, 'Tue Feb 21, 2023', '4pm - 5pm (EST).', 3, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (5, 1, 'Fusing Symbolic and Subsymbolic Approaches for Natural and Effective Human-Robot Collaboration', 4, 3, 'Monday, February 27, 2023', '11:45am (EST)', 0, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (6, 3, 'SIGecom Winter Meeting', 8, 6, 'Wednesday, February 22nd', '11am - 5pm ET.', 6, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (7, 2, 'Reinforcement Learning for Automated Exploration and Detection of Cache-Timing Attacks', 5, 4, 'Thu Feb 16, 2023', '4pm - 5pm (EST).', 6, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (8, 1, 'Messages, Secrets, and Catalysts in Population Protocols with Probabilistic Scheduling', 6, 5, 'Monday, March 20, 2023', '4 PM (ET)', 4, 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, department_id) VALUES (9, 3, 'NA', 7, 6, 'NA', '2:30 - 3:50 p.m.', 5, 0)")


    # print the databases if verbose is true
    if verbose:
        test = c.execute("SELECT * FROM types")
        print(test.fetchall())
        test = c.execute("SELECT * FROM speakers")
        print(test.fetchall())
        test = c.execute("SELECT * FROM hosts")
        print(test.fetchall())
        test = c.execute("SELECT * FROM locations")
        print(test.fetchall())
        test = c.execute("SELECT * FROM departments")
        print(test.fetchall())
        test = c.execute("SELECT * FROM events")
        print(test.fetchall())

    # Save (commit) the changes, and then close the connection
    conn.commit()
    conn.close()

def main():
    os.remove('events.db')          # delete the database if it already exists. Only used for ease of testing

    print("Creating database...")
    createDatabase()

    # printDatabases = False      # True or False. If true, the databases will be printed after they are populated. WARNING: This will print a lot of data
    # populateDatabaseOld(printDatabases)

    print("Populating database...")
    populateDatabase(True)

    # print("\nTesting searchEventsDatabase():")
    # events = searchEventsDatabase()
    # for event in events:
    #     print(type(event))
    #     print(event)

    # print("\nTesting searchEventsDatabase('Feimster'):")
    # for event in searchEventsDatabase('Feimster'):
    #     print(event)

if __name__ == '__main__':
    main()
