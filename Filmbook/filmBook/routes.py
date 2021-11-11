#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Init for FilmBook app project"""
# =============================================================================
# Imports
# =============================================================================
from flask import render_template
from filmBook import app


@app.route('/')
@app.route('/index')
def index():
    """Rout for index.html"""

    user = {'username': 'Dima'}
    return render_template('index.html', title='FilmBook', user=user)
