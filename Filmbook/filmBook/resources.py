#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Resources for routes.py """
# =============================================================================
# Imports
# =============================================================================
from flask_restx import fields, reqparse
from filmBook import api


"""For GET: /film """
films_model = api.model(
    'films',
    {
        'film': fields.String(),
        'film_id': fields.Integer(),
        'film_name': fields.String(),
        'rated': fields.String(),
        'poster_url': fields.String(),
        'release_date': fields.Date(),
        'rating': fields.Float(),
        'nickname': fields.String(),
        'imdb_id': fields.String(),
        'description': fields.String(),
        'genres': fields.String(),
        'directors': fields.String()
    }
    )


films_get_parser = api.parser()
films_get_parser.add_argument('page', type=int, default=1)
films_get_parser.add_argument('name', type=str, default='')
films_get_parser.add_argument('genre', type=str, default=None)
films_get_parser.add_argument('director', type=str, default=None)
films_get_parser.add_argument('rel_start', type=int, default=1900)
films_get_parser.add_argument('rel_fin', type=int, default=2100)
films_get_parser.add_argument('order', type=str, default=None)

"""For DELETE: /films """
delete_films_model = api.model(
    'films',
    {
        'status': fields.Boolean(),
    }
    )


"""For POST: /add_films """
add_films_model = api.model(
    'films',
    {
        'film_id': fields.Integer(),
    }
    )

add_films_post_parser = reqparse.RequestParser(bundle_errors=True)
add_films_post_parser.add_argument('imdb_id', type=str, default='')
add_films_post_parser.add_argument('film_name', type=str)
add_films_post_parser.add_argument('rated', type=str)
add_films_post_parser.add_argument('poster_url', type=str, default=None)
add_films_post_parser.add_argument('release_date', type=str, default=None)
add_films_post_parser.add_argument('rating', type=float, default=9.0)
add_films_post_parser.add_argument('genre', type=str, action='split', default=['Art-house'])
add_films_post_parser.add_argument('director', type=str, action='split', default=['Noname'])
add_films_post_parser.add_argument('description', type=str, default=None)


"""For UPDATE: /add_films """
update_films_model = api.model(
    'films',
    {
        'film_id': fields.Boolean(),
    }
    )

update_films_parser = reqparse.RequestParser(bundle_errors=True)
update_films_parser.add_argument('imdb_id', type=str, default=None)
update_films_parser.add_argument('film_name', type=str, default=None)
update_films_parser.add_argument('rated', type=str, default=None)
update_films_parser.add_argument('poster_url', type=str, default=None)
update_films_parser.add_argument('release_date', type=str, default=None)
update_films_parser.add_argument('rating', type=float, default=None)
update_films_parser.add_argument('genre', type=str, action='split', default=[None])
update_films_parser.add_argument('director', type=str, action='split', default=[None])
update_films_parser.add_argument('description', type=str, default=None)



"""For delete director"""
dir_name_parser = api.parser()
dir_name_parser.add_argument('name', type=str)

dir_name_model = api.model(
    'director',
    {
        'status': fields.Boolean(),
    }
    )


"""For POST: /registration """
add_user_model = api.model(
    'films',
    {
        'status': fields.Integer(),
    }
    )

add_user_post_parser = reqparse.RequestParser(bundle_errors=True)
add_user_post_parser.add_argument('nickname', type=str)
add_user_post_parser.add_argument('email', type=str)
add_user_post_parser.add_argument('password', type=str)


"""For POST: /login """
login_user_model = api.model(
    'films',
    {
        'error': fields.String(),
        'status': fields.Boolean(),
    }
    )

login_user_post_parser = reqparse.RequestParser(bundle_errors=True)
login_user_post_parser.add_argument('nickname', type=str)
login_user_post_parser.add_argument('password', type=str)


"""For POST: /logout """
logout_user_model = api.model(
    'films',
    {
        'id': fields.Integer(),
        'status': fields.Boolean(),
    }
    )
#
# logout_user_post_parser = reqparse.RequestParser(bundle_errors=True)
# logout_user_post_parser.add_argument('nickname', type=str)
# logout_user_post_parser.add_argument('password', type=str)