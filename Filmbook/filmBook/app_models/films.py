#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database app_models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from datetime import date
from filmBook import db
from filmBook.app_models.associatin_tables import films_directors
from filmBook.app_models.associatin_tables import films_genres

class Films(db.Model):
    """Main film table"""
    __tablename__ = 'films'
    film_id = db.Column(db.Integer, primary_key=True)
    film_name = db.Column(db.Text, unique=False, nullable=False, index=True)
    rateds_rated_id = db.Column(
        db.Integer, db.ForeignKey('rateds.rated_id'),
        unique=False, nullable=False)
    poster_url = db.Column(db.Text, unique=True, nullable=False)
    release_date = db.Column(db.Date, unique=False, nullable=False, index=True)
    rating = db.Column(db.Float, unique=False, nullable=False, index=True)
    user_added = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    imdb_id = db.Column(db.String(10), unique=True)
    description = db.Column(db.Text, unique=False, nullable=True, index=True)

    # for association
    # film_genr = db.relationship(
    #     'Genres', secondary=films_genres, lazy='subquery',
    #     backref=db.backref('films_gen', lazy=True))
    #
    # film_direc = db.relationship(
    #     'Directors', secondary=films_directors, lazy='subquery',
    #     backref=db.backref('films_dir', lazy=True))

    def __init__(self, film_name: str, rated: int, poster_url: str,
                 release_date: str, rating: float, user_added: int,
                 imdb_id: str = None,  description: str = None):

        self.imdb_id = imdb_id
        self.film_name = film_name
        self.rateds_rated_id = rated
        self.poster_url = poster_url
        self.release_date = release_date
        self.rating = rating
        self.description = description
        self.user_added = user_added

    def __repr__(self):
        return f'film_id:{self.film_id},film_name:{self.film_name},' \
               f'rated:{self.rateds_rated_id},poster_url:{self.poster_url}' \
               f'release_date: {self.release_date},rating:{self.rating},' \
               f'user_added: {self.user_added},description:{self.description}'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
