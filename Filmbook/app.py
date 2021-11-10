#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Start app"""
# =============================================================================
# Imports
# =============================================================================
from filmBook import app


@app.route('/')
def hello_world():  # put application's code here
    """Temple route"""
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
