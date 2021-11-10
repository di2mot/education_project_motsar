#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Init for Filmbook app project"""
# =============================================================================
# Imports
# =============================================================================
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Constants
DBNAME = "filmbook"
DIALECT = "postgresql"
DRIVER = "psycopg2"
LOGIN = "postgres"
PASS = "changeme"
HOST = "localhost"
CONF_KEY = "SQLALCHEMY_DATABASE_URI"

# Connecting
app = Flask(__name__)
app.config[CONF_KEY] = f'{DIALECT}+{DRIVER}://{LOGIN}:{PASS}@{HOST}/{DBNAME}'
db = SQLAlchemy(app)
