"""Initialization of events blueprint"""
from flask import Blueprint
bp_events = Blueprint('events', __name__)

from app.users import routes