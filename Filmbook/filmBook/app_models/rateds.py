#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database app_models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import db

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