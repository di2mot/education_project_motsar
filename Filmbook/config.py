#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Config for migrate"""
# =============================================================================
# Imports
# =============================================================================

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Config fo DB connection"""

    # For postgres
    db_name = "filmbook"
    dialect = "postgresql"
    driver = "psycopg2"
    login = "postgres"
    passw = "changeme"
    host = "localhost"

    # For SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'filmbook.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # For postgres
    # SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{driver}://{login}:{passw}@{host}/{db_name}'
