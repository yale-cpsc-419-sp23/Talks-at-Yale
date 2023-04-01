"""
This represent the database models, which are classes, such as Users, Events, etc
"""
from hashlib import sha256
from app import db
from flask_login import UserMixin


# create association table
favorites = db.Table('favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)
class Event(db.Model):
    """A class representing an event"""
    id = db.Column(db.Integer, primary_key=True)
    event_hash = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=False)
    speaker = db.Column(db.String, nullable=True)
    speaker_title = db.Column(db.String, nullable=True)
    host = db.Column(db.String, nullable=True)
    department = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    iso_date = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=True)
    bio = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    is_upcoming = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        """How the object event will be represented"""
        return '<Event {}>'.format(self.id)

    def generate_hash(self):
        """Generating hash for an event"""
        sha = sha256()
        sha.update(f'{self.title}{self.date}{self.time}{self.iso_date}'.encode('utf-8'))
        return sha.hexdigest()
    @classmethod
    def event_exists(cls, title, date, time, iso_date):
        """Class method that returns true if an event already exist"""
        event_hash = cls.generate_hash_static(title, date, time, iso_date)
        return cls.query.filter_by(event_hash=event_hash).first() is not None
    @staticmethod
    def generate_hash_static(title, date, time, iso_date):
        """Static method that generates hash"""
        sha = sha256()
        sha.update(f'{title}{date}{time}{iso_date}'.encode('utf-8'))
        return sha.hexdigest()

    def to_dict(self):
        """A function that represent an event as a dict"""
        return {
            'id' : self.id,
            'type' : self.type,
            'title' : self.title,
            'speaker' : self.speaker,
            'speaker_title' : self.speaker_title,
            'host' : self.host,
            'department' : self.department,
            'date' : self.date,
            'time' : self.time,
            'location' : self.location,
            'bio' : self.bio,
            'description' : self.description,
        }


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    netid = db.Column(db.String(80), unique=True)
    favorite_events = db.relationship('Event', secondary=favorites, backref=db.backref('favorited_by', lazy='dynamic'))
    email = db.Column(db.String, nullable=True)
    first_name = db.Column(db.String, unique=False, nullable=True)
    last_name = db.Column(db.String, unique=False, nullable=True)
    year = db.Column(db.String, unique=False, nullable=True)
    college = db.Column(db.String, unique=False, nullable=True)
    birthday = db.Column(db.String, unique=False, nullable=True)
    major = db.Column(db.String, unique=False, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def profile(self):
        """Dict of user profile"""
        return {
            'email': self.email,
            'fist_name': self.first_name,
            'last_name': self.last_name,
            'year': self.year,
            'college': self.college,
            'birthday': self.birthday,
            'major': self.major,
        }