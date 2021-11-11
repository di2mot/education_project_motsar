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
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    second_name = db.Column(db.String(20), unique=True, nullable=False)
    film = db.relationship('films', secondary=films_directors, lazy='subquery',
                           backref=db.backref('directors', lazy=True))

    def __init__(self, first_name: str, second_name: str):
        self.first_name = first_name
        self.second_name = second_name

    def __repr__(self):
        return f'<Directors: first name: {self.first_name}, second name: {self.second_name}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
