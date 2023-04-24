"""Initialization of user blueprint"""
from flask import Blueprint
bp_users = Blueprint('users', __name__)

from app.users import routes