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
    'films_directors',
    db.Column('films_film_id', db.Integer, db.ForeignKey('films.film_id', ondelete="CASCADE")),
    db.Column('directors_director_id', db.Integer, db.ForeignKey('directors.director_id', ondelete="CASCADE"))
    )

# Association table for table films and table genres
films_genres = db.Table(
    'films_genres',
    db.Column('films_film_id', db.Integer, db.ForeignKey('films.film_id', ondelete="CASCADE")),
    db.Column('genres_genre_id', db.Integer, db.ForeignKey('genres.genre_id', ondelete="CASCADE"))
    )
