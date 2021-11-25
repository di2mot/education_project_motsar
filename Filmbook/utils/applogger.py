#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Logger siting for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from logging.config import dictConfig
from logging.handlers import RotatingFileHandler
from logging import Formatter
import logging
from filmBook import app

app.config.from_object('config.DevelopmentConfig')
handler = RotatingFileHandler(app.config['LOGFILE'],
                              maxBytes=1000000, backupCount=1)
handler.setLevel(logging.DEBUG)
handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '
                               '[in %(pathname)s:%(lineno)d]'))
# logging.disable(logging.CRITICAL)  # Расскоментарь это для прекращения логов
app.logger.addHandler(handler)

log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
log.addHandler(handler)
