#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Init for FilmBook app project"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import login_manager
from filmBook.db_core import get_user_nickname


@login_manager.user_loader
def load_user(id):
    return get_user_nickname(int(id))
