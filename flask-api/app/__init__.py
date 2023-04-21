"""
Initialization of the flask app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cas import CAS
from flask_cors import CORS
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cas = CAS(app)
# Add the CORS configuration
CORS(app, resources={r"/*": {"origins": "*", 'supports_credentials': True}})
jwt = JWTManager(app)

# Registering users blueprint
from app.users import bp_users
app.register_blueprint(bp_users)

# registering events blueprint
from app.events import bp_events
# app.register_blueprint(bp_events)
app.register_blueprint(bp_events, url_prefix='/events')

from app import models
