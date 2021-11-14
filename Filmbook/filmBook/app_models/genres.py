#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database app_models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import db
from filmBook.app_models.associatin_tables import films_genres


class Genres(db.Model):
    """Table with genres"""

    __tablename__ = 'genres'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(20), unique=True, nullable=False)
    film_genr = db.relationship(
        'Films', secondary=films_genres, lazy='subquery',
        backref=db.backref('gen_films', lazy=True))

    def __init__(self, genre_name: str):
        self.genre_name = genre_name

    def __repr__(self):
        return f'<Genre:  genre: {self.genre_name}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)