#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Association table for tables table films, table directors, table  genres"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import db

# Association table for table films and table directors
films_directors = db.Table(
    'films_directors', db.Model.metadata,
    db.Column('films_film_id', db.Integer,
    db.ForeignKey('films.film_id')),
    db.Column('directors_director_id', db.Integer,
        db.ForeignKey('directors.director_id'))
    )

# Association table for table films and table genres
films_genres = db.Table(
    'films_genres', db.Model.metadata,
    db.Column('films_film_id', db.Integer, db.ForeignKey('films.film_id')),
    db.Column('genres_genre_id', db.Integer, db.ForeignKey('genres.genre_id'))
    )