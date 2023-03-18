"""Application configuration go into this file"""
import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Configuration keys and their values"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'events.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'project-group-1'
    CAS_SERVER = 'https://secure.its.yale.edu/cas'
    CAS_LOGIN_ROUTE = '/login'
    CAS_AFTER_LOGIN = 'after_login'
    # CAS_VERIFY_SSL = False
    CAS_LOGOUT_ROUTE = '/logout'
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = "None"
    CAS_VERSION = '2.0'
    # SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SESSION_TYPE = 'filesystem'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'oursecretkey'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)