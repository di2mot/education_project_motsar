#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database app_models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from datetime import datetime
from filmBook import db
from filmBook.app_models.associatin_tables import films_directors
from filmBook.app_models.associatin_tables import films_genres

class Films(db.Model):
    """Main film table"""
    __tablename__ = 'films'
    film_id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String(10), unique=True)
    film_name = db.Column(db.Text, unique=False, nullable=False, index=True)
    rateds_rated_id = db.Column(
        db.Integer, db.ForeignKey('rateds.rated_id'),
        unique=False, nullable=False)
    poster_url = db.Column(db.Text, unique=True, nullable=False)
    release_date = db.Column(db.Date, unique=False, nullable=False, index=True)
    rating = db.Column(db.Integer, unique=False, nullable=False, index=True)
    description = db.Column(db.Text, unique=False, index=True)
    user_added = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    # for association
    film_genr = db.relationship(
        'films', secondary=films_genres, lazy='subquery',
        backref=db.backref('genres', lazy=True))
    film_direc = db.relationship(
        'films', secondary=films_directors, lazy='subquery',
        backref=db.backref('directors', lazy=True))

    def __init__(self, film_name: str, rateds_rated_id: int, poster_url: str,
                 release_date: datetime, rating: int, user_added: int):
        self.film_name = film_name
        self.rateds_rated_id = rateds_rated_id
        self.poster_url = poster_url
        self.release_date = release_date
        self.rating = rating
        self.user_added = user_added

    def __repr__(self):
        return f'<Films: title: {self.film_name}, release date: {self.release_date}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)