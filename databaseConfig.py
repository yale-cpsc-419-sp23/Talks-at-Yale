import sqlite3
import os
from flask import Flask
from json import dumps
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/events/<searchTerm>')
def searchEventsDatabase(searchTerm):
    """returns a list of events that match the search term"""
    print(searchTerm)
    c = sqlite3.connect('events.db')
    query = """SELECT * 
        FROM events
        LEFT JOIN speakers ON events.speaker_id = speakers.id
        LEFT JOIN hosts ON events.host_id = hosts.id
        WHERE title LIKE :searchTerm OR speaker_name LIKE :searchTerm OR host_name LIKE :searchTerm"""
    events = c.execute(query, {"searchTerm": f'%{searchTerm}%'})
    # print(events.fetchall())
    return dumps(events.fetchall())


def getEventsDatabase():
    """returns the database object"""
    c = sqlite3.connect('events.db')
    events = c.execute("SELECT * FROM events")
    return events

def createDatabase():
    # Connect to a database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('events.db')

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Create the tables

    c.execute('''CREATE TABLE types(
                id INTEGER,
                type TEXT,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE speakers(
                id INTEGER,
                speaker_name TEXT,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE hosts(
                id INTEGER,
                host_name TEXT,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE locations(
                id INTEGER,
                location TEXT,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE departments(
                id INTEGER,
                department TEXT,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE events(
                id INTEGER,
                type_id INTEGER,
                title TEXT,
                speaker_id INTEGER,
                host_id INTEGER,
                date TEXT,
                time TEXT,
                location_id INTEGER,
                info TEXT,
                department_id INTEGER,
                FOREIGN KEY (type_id) REFERENCES types(id),
                FOREIGN KEY (speaker_id) REFERENCES speakers(id),
                FOREIGN KEY (host_id) REFERENCES hosts(id),
                FOREIGN KEY (location_id) REFERENCES locations(id),
                FOREIGN KEY (department_id) REFERENCES departments(id),
                PRIMARY KEY (id, department_id, type_id, speaker_id, host_id, location_id))''')

    # Save (commit) the changes, and then close the connection
    conn.commit()
    conn.close()

def populateDatabase(verbose=False):
    """adds preformatted events to the created database."""

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
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (0, 0, 'CS Talk - Faculty Recruit', 'Jay Lim', 0, 'Tuesday, February 28', '4:00 p.m.', 0, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (1, 1, 'Automatically Preventing, Detecting, and Repairing Crucial Errors in Programs', 1, 0, 'March 6th, 2023', '1 PM EST.', 1, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (2, 2, 'NA', 2, 2, 'Thursday, March 9, 2023', '10:00 AM.', 6, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (3, 3, 'Robot Abuse: Is it okay for me to hit my robot?', 8, 6, 'February 28', '5:00 p.m.', 2, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (4, 0, 'Learning Systems in Adaptive Environments. Theory, Algorithms and Design', 3, 2, 'Tue Feb 21, 2023', '4pm - 5pm (EST).', 3, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (5, 1, 'Fusing Symbolic and Subsymbolic Approaches for Natural and Effective Human-Robot Collaboration', 4, 3, 'Monday, February 27, 2023', '11:45am (EST)', 0, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (6, 3, 'SIGecom Winter Meeting', 8, 6, 'Wednesday, February 22nd', '11am - 5pm ET.', 6, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (7, 2, 'Reinforcement Learning for Automated Exploration and Detection of Cache-Timing Attacks', 5, 4, 'Thu Feb 16, 2023', '4pm - 5pm (EST).', 6, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (8, 1, 'Messages, Secrets, and Catalysts in Population Protocols with Probabilistic Scheduling', 6, 5, 'Monday, March 20, 2023', '4 PM (ET)', 4, 'This is a work in progress', 0)")
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (9, 3, 'NA', 7, 6, 'NA', '2:30 - 3:50 p.m.', 5, 'This is a work in progress', 0)")


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
    createDatabase()

    printDatabases = 0
    populateDatabase(printDatabases)

    # events = getEventsDatabase()
    # for event in events:
    #     print(type(event))
    #     print(event)

    # for event in searchEventsDatabase('Ruzica'):
    #     print(event)
    # print(searchEventsDatabase('Ruzica'))

if __name__ == '__main__':
    app.run(debug=True)
    # main()
