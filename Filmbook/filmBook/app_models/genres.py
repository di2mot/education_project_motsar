#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database app_models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import db


class Genres(db.Model):
    """Table with genres"""

    __tablename__ = 'genres'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, genre: str):
        self.genre = genre

    def __repr__(self):
        return f'<Genre:  genre: {self.genre}>'
        # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)