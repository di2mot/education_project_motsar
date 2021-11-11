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
from config import Config

# Connecting
app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Import routes and models
from filmBook import routes, models
