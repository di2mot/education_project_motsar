#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Init for FilmBook app project"""
# =============================================================================
# Imports
# =============================================================================
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restx import Api
from config import DBconfig

# Create Flask app
app = Flask(__name__)
app.debug = True
# for resources
api = Api(app, version="1.0", title="FilmBook API", description="A simple API")

# part for users logins
login_manager = LoginManager(app)
login_manager.init_app(app)


# DB config
app.config.from_object(DBconfig)

# init SQLAlchemy
db = SQLAlchemy(app)

# init migration
migrate = Migrate(app, db)

# Import routes and models
from filmBook import routes, models
from filmBook.app_models import auth
from utils import applogger

