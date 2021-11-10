#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Init for FilmBook app project"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    """Rout for index.html"""
    user = {'username': 'Miguel'}
    return render_template('index.html', title='FilmBook', user=user)
