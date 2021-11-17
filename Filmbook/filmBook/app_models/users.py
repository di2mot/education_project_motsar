#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database app_models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import db
from flask_login import UserMixin


# Tables
class Users(UserMixin, db.Model):
    """Table for Users"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, nickname: str, email: str, password: str):
        self.nickname = nickname
        self.email = email
        self.password = password


    # def __repr__(self):
    #     return f'<User: nickname: {self.nickname}, email: {self.email}>'
    #     # return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
