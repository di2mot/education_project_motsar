#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Config for migrate"""
# =============================================================================
# Imports
# =============================================================================



class Config:
    """Config fo DB connection"""

    # For postgres
    db_name = "filmbook"
    dialect = "postgresql"
    # if not work, use  pg8000
    driver = "psycopg2"
    login = "postgres"
    passw = "postgres_password"
    host = "localhost"

    # For SQLite
    # import os
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'filmbook.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'DEV'

    # For postgres
    SQLALCHEMY_DATABASE_URI = f'{dialect}+{driver}://{login}:{passw}@{host}/{db_name}'
