"""
This represent the database models, which are classes, such as Users, Events, etc
"""
from hashlib import sha256
from app import db
from flask_login import UserMixin

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


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'