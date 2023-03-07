import sqlite3
import os

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
                name TEXT,
                PRIMARY KEY (id))''')

    c.execute('''CREATE TABLE hosts(
                id INTEGER,
                name TEXT,
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



    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()

def populateDatabase(verbose=False):
    """adds preformatted events to the created database."""

    # Connect to a database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('events.db')

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # populates the types table
    c.execute("INSERT INTO types (type, id) VALUES ('CS Talk - Faculty Recruit', 0)")
    c.execute("INSERT INTO types (type, id) VALUES ('Dissertation Defense', 1)")
    c.execute("INSERT INTO types (type, id) VALUES ('EE Seminar', 2)")
    c.execute("INSERT INTO types (type, id) VALUES ('other', 3)")

    if verbose:
        test = c.execute("SELECT * FROM types")
        print(test.fetchall())

    # populates the speakers table
    c.execute("INSERT INTO speakers (name, id) VALUES ('Jay Lim', 0)")
    c.execute("INSERT INTO speakers (name, id) VALUES ('Jialu Zhang', 1)")
    c.execute("INSERT INTO speakers (name, id) VALUES ('Dr. Shuwen Deng', 2)")
    c.execute("INSERT INTO speakers (name, id) VALUES ('Aldo Pacchiano', 3)")
    c.execute("INSERT INTO speakers (name, id) VALUES ('Jake Brawer', 4)")
    c.execute("INSERT INTO speakers (name, id) VALUES ('Wenjie Xiong', 5)")
    c.execute("INSERT INTO speakers (name, id) VALUES ('Talley Amir', 6)")
    c.execute("INSERT INTO speakers (name, id) VALUES ('Weijie Su', 7)")
    c.execute("INSERT INTO speakers (name, id) VALUES ('NA', 8)")

    if verbose:
        test = c.execute("SELECT * FROM speakers")
        print(test.fetchall())

    # populates the hosts table
    c.execute("INSERT INTO hosts (name, id) VALUES ('Ruzica Piskac', 0)")
    c.execute("INSERT INTO hosts (name, id) VALUES ('Professor Jakub Szefer', 1)")
    c.execute("INSERT INTO hosts (name, id) VALUES ('Steve Zucker', 2)")
    c.execute("INSERT INTO hosts (name, id) VALUES ('Brian Scassellati', 3)")
    c.execute("INSERT INTO hosts (name, id) VALUES ('Jakub Szefer', 4)")
    c.execute("INSERT INTO hosts (name, id) VALUES ('James Aspnes', 5)")
    c.execute("INSERT INTO hosts (name, id) VALUES ('NA', 6)")

    if verbose:
        test = c.execute("SELECT * FROM hosts")
        print(test.fetchall())

    # populates the locations table
    c.execute("INSERT INTO locations (location, id) VALUES ('AWK 200', 0)")
    c.execute("INSERT INTO locations (location, id) VALUES ('AKW 307', 1)")
    c.execute("INSERT INTO locations (location, id) VALUES ('LC 105', 2)")
    c.execute("INSERT INTO locations (location, id) VALUES ('AKW 200, 51 Prospect Street', 3)")
    c.execute("INSERT INTO locations (location, id) VALUES ('TBD', 4)")
    c.execute("INSERT INTO locations (location, id) VALUES ('87 Trumbull St, Room B120', 5)")
    c.execute("INSERT INTO locations (location, id) VALUES ('NA', 6)")

    if verbose:
        test = c.execute("SELECT * FROM locations")
        print(test.fetchall())

    # populates the departments table
    c.execute("INSERT INTO departments (department, id) VALUES ('Computer Science', 0)")

    if verbose:
        test = c.execute("SELECT * FROM departments")
        print(test.fetchall())

    # populates the events table
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (0, 0, 'CS Talk - Faculty Recruit', 0, 0, 'Tuesday, February 28', '4:00 p.m.', 0, 'This is a work in progress', 0)")       # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (1, 1, 'Automatically Preventing, Detecting, and Repairing Crucial Errors in Programs', 1, 0, 'March 6th, 2023', '1 PM EST.', 1, 'This is a work in progress', 0)")      # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (2, 2, 'NA', 2, 2, 'Thursday, March 9, 2023', '10:00 AM.', 6, 'This is a work in progress', 0)")       # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (3, 3, 'Robot Abuse: Is it okay for me to hit my robot?', 8, 6, 'February 28', '5:00 p.m.', 2, 'This is a work in progress', 0)")      # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (4, 0, 'Learning Systems in Adaptive Environments. Theory, Algorithms and Design', 3, 2, 'Tue Feb 21, 2023', '4pm - 5pm (EST).', 3, 'This is a work in progress', 0)")     # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (5, 1, 'Fusing Symbolic and Subsymbolic Approaches for Natural and Effective Human-Robot Collaboration', 4, 3, 'Monday, February 27, 2023', '11:45am (EST)', 0, 'This is a work in progress', 0)")     # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (6, 3, 'SIGecom Winter Meeting', 8, 6, 'Wednesday, February 22nd', '11am - 5pm ET.', 6, 'This is a work in progress', 0)")    # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (7, 2, 'Reinforcement Learning for Automated Exploration and Detection of Cache-Timing Attacks', 5, 4, 'Thu Feb 16, 2023', '4pm - 5pm (EST).', 6, 'This is a work in progress', 0)")       # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (8, 1, 'Messages, Secrets, and Catalysts in Population Protocols with Probabilistic Scheduling', 6, 5, 'Monday, March 20, 2023', '4 PM (ET)', 4, 'This is a work in progress', 0)")    # done
    c.execute("INSERT INTO events (id, type_id, title, speaker_id, host_id, date, time, location_id, info, department_id) VALUES (9, 3, 'NA', 7, 6, 'NA', '2:30 - 3:50 p.m.', 5, 'This is a work in progress', 0)")    # done

    if verbose:
        test = c.execute("SELECT * FROM events")
        print(test.fetchall())



    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()


def main():
    os.remove('events.db')          # delete the database if it already exists. Only used for ease of testing
    createDatabase()

    printDatabases = False
    populateDatabase(printDatabases)

if __name__ == '__main__':
    main()
