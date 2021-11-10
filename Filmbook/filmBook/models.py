#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import db


# Tables
class Users(db.Model):
    """Table for Users"""

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User: nickname: {self.nickname}, email: {self.email}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


# Association table for table films and table directors
films_directors = db.Table(
    'films_directors', db.Model.metadata,
    db.Column('films_film_id', db.Integer,
    db.ForeignKey('films.film_id')),
    db.Column('directors_director_id', db.Integer,
    db.ForeignKey('directors.director_id')
    )
                            )

# Association table for table films and table genres
films_genres = db.Table(
    'films_genres', db.Model.metadata,
    db.Column('films_film_id', db.Integer, db.ForeignKey('films.film_id')),
    db.Column('genres_genre_id', db.Integer, db.ForeignKey('genres.genre_id'))
    )


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

    def __init__(self, film_name, rateds_rated_id, poster_url, release_date, rating, user_added):
        self.film_name = film_name
        self.rateds_rated_id = rateds_rated_id
        self.poster_url = poster_url
        self.release_date = release_date
        self.rating = rating
        self.user_added = user_added

    def __repr__(self):
        return f'<Films: title: {self.film_name}, release date: {self.release_date}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


class Rateds(db.Model):
    """Rated of film like PG-13"""

    __tablename__ = 'rateds'
    rated_id = db.Column(db.Integer, primary_key=True)
    rated = db.Column(db.String(5), unique=True, nullable=False)

    def __init__(self, rated):
        self.rated = rated

    def __repr__(self):
        return f'<Rated: rated: {self.rated}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


class Genres(db.Model):
    """Table with genres"""

    __tablename__ = 'genres'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(20), unique=True, nullable=False)
    film = db.relationship('films', secondary=films_genres, lazy='subquery',
                           backref=db.backref('genres', lazy=True))

    def __init__(self, genre):
        self.genre = genre

    def __repr__(self):
        return f'<Genre:  genre: {self.genre}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


class Directors(db.Model):
    """Table with genres"""

    __tablename__ = 'directors'
    director_d = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    second_name = db.Column(db.String(20), unique=True, nullable=False)
    film = db.relationship('films', secondary=films_directors, lazy='subquery',
                           backref=db.backref('directors', lazy=True))

    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def __repr__(self):
        return f'<Directors: first name: {self.first_name}, second name: {self.second_name}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
