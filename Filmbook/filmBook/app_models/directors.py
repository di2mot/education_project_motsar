#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database app_models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import db
from filmBook.app_models.associatin_tables import films_directors


class Directors(db.Model):
    """Table with genres"""

    __tablename__ = 'directors'
    director_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    film_direc = db.relationship(
        'Films', secondary=films_directors, lazy='subquery',
        backref=db.backref('dir_films', lazy=True))

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'<Directors: name: {self.name}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
