#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Database app_models classes for Filmbook app"""
# =============================================================================
# Imports
# =============================================================================
from filmBook.models import Films
from filmBook.models import Genres
from filmBook.models import Rateds
from filmBook.models import Directors
from filmBook.models import Users
from filmBook import db


def get_user_id(nickname: str) -> int:
    """
    Input: str - nickname of user from table users.nickname
    Output: int - user id in table users.user_id
    """

    if not isinstance(nickname, str):
        raise TypeError(f'Type nickname must bi <class "str"> not {type(nickname)}')

    user_id = Users.query.filter_by(nickname=nickname).first()

    if user_id is None:
        return user_id
    return user_id.user_id


def get_user_nickname(user_id: str) -> str:
    """
    Input: int - user_id of user from table users.user_id
    Output: str - nickname of user from table users.nickname
    """

    if not isinstance(user_id, int):
        return f'TypeError: Type user_id must bi <class "int"> not {type(user_id)}'

    user_nick = Users.query.filter_by(user_id=user_id).first()

    return user_nick.nickname


def get_user_password(user_id: str) -> str:
    """
    Input: int - user_id of user from table users.user_id
    Output: str - nickname of user from table users.nickname
    """

    if not isinstance(user_id, int):
        return f'TypeError:Type user_id must bi <class "int"> not {type(user_id)}'

    user_pass = Users.get(user_id)

    return user_pass.password


def add_new_user(nickname: str, email: str, password: str) -> str:
    """Create new user
    Input nickname : str - user nickname, min len=3 max len=20,
    Input email : str - user email, min len=5 max len=20,
    Input password : str - user password, min len=8 max len=120

    Output: str - user_id of new user
    If there is an error in user input, it returns an exception with a description of the error."""

    # Check correct input
    if not isinstance(nickname, str):
        return f'TypeError: nickname type must be <class "str", not {type(nickname)}>'
    if not isinstance(email, str):
        return f'TypeError: email type must be <class "str", not {type(email)}>'
    if not isinstance(password, str):
        return f'TypeError: password type must be <class "str", not {type(password)}>'
    if not 3 <= len(nickname) <= 20:
        return 'ValueError: nickname length must be between 3 and 20 characters, ' \
               f'you nickname length={len(nickname)}'
    if not 5 <= len(email) <= 20:
        return 'ValueError: email length must be between 5 and 20 characters, ' \
                f'you nickname length={len(email)}'
    if not 0 <= len(password) <= 120:
        return f'ValueError: email length must be between 8 and 120 characters, ' \
               f'you nickname length={len(password)}'

    try:
        # Check the availability of the name
        if get_user_id(nickname=nickname) is not None:
            return f'NicknameError: nickname {nickname} is already taken'
        new_user = Users(nickname=nickname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        # get user_id of new user
        user_id = get_user_id(nickname=nickname)
        return str(user_id)

    except Exception as error:
        print(error)
        return 'ServerError: Something went wrong'


def get_genre(genre: str = None, genre_id: int = None) -> str:
    """
    Input: str - name of genre from table genres.genre
        or
    Input: int - genre_id of genre from table genres.genre

    Output: str - genre_id in table genres.genre_id
        or
    Output: str - genre_id in table genres.genre_id
    """

    if genre is not None:
        if not isinstance(genre, str):
            raise TypeError(f'Type genre must bi <class "str"> not {type(genre)}')

        genre_id = Genres.query.filter_by(genre_name=str(genre)).first()

        if genre_id is None:

            return genre_id

        return genre_id

    if genre_id is not None:
        if not isinstance(genre, str):
            raise TypeError(f'Type genre must bi <class "int"> not {type(genre)}')

        genre_id = Genres.get(genre_id)

        return str(genre_id.genre)


def add_new_genre(genre: str) -> str:
    """Create new genre
    Input genre : str - film genre, min len=2 max len=20,

    Output: str - genre_id
    If there is an error in user input, it returns an exception with a description of the error."""

    # Check correct input
    if not isinstance(genre, str):
        return f'TypeError: genre type must be <class "str", not {type(genre)}>'

    if not 2 <= len(genre) <= 20:
        return 'ValueError: genre length must be between 2 and 20 characters, ' \
               f'you genre length={len(genre)}'

    try:
        # if get_genre(genre=genre) is not None:
        #     return 'This genre already exists'

        new_genre = Genres(genre_name=genre)
        db.session.add(new_genre)
        db.session.commit()
        print(158)
        # get user_id of new user
        genre_id = get_genre(genre=genre)
        return genre_id

    except Exception as error:
        print(error)

    finally:
        return 'ServerError: Something went wrong'


def get_director(name: str = None, director_id: int = None) -> str:
    """
    Input: name: str - name of director from table directors.first_name
        or
    Input: director_id: int - director_id of director from table
                              directors.director_id

    Output: director_id: str - director_id in table directors.director_id
        or
    Output: str - genre_id in table genres.genre_id
    """
    if name is not None:
        if not isinstance(name, str):
            raise TypeError(f'Type name must be <class "str"> not {type(name)}')

        dir_id = Directors.query.filter_by(name=name).first()

        if dir_id is None:
            return dir_id

        return dir_id.director_id

    if director_id is not None:
        if not isinstance(director_id, int):
            raise TypeError(f'Type director_id must be <class "int"> not {type(director_id)}')

        dir_id = Directors.get(director_id)

        return str(dir_id.name)


def add_new_director(name: str) -> str:
    """Create new genre
    Input name : str - director name, min len=2 max len=40,

    Output: dir_id: str - director_id
    If there is an error in user input, it returns an exception with a description of the error."""

    # Check correct input
    if not isinstance(name, str):
        return f'TypeError: nickname type must be <class "str", not {type(name)}>'

    if not 2 <= len(name) >= 40:
        return 'ValueError: nickname length must be between 2 and 20 characters, ' \
               f'you nickname length={len(name)}'

    try:
        if get_director(name) is not None:
            return 'This genre already exists'

        new_gir = Directors(name=name)
        db.session.add(new_gir)
        db.session.commit()

        # get user_id of new user
        dir_id = get_genre(name)
        return str(dir_id)

    except Exception as error:
        print(error)


def get_rated(rated: str = None, rated_id: int = None) -> str:
    """
    Input: str - name of rated from table rateds.rated
        or
    Input: int - rated_id of rated from table rateds.rated

    Output: rated_id: str - rated_id in table rateds.rated_id
        or
    Output: rated: str - rated in table rateds.rated
    """
    if rated is not None:
        if not isinstance(rated, str):
            raise TypeError(f'Type genre must bi <class "str"> not {type(rated)}')

        res_rated = Rateds.query.filter_by(rated=rated).first()

        return str(res_rated.rated_id)

    if rated_id is not None:
        if not isinstance(rated, str):
            raise TypeError(f'Type rated must bi <class "int"> not {type(rated)}')

        res_rated = Rateds.get(rated_id)

        return res_rated.rated


def add_new_rated(rated: str) -> str:
    """Create new genre
    Input rated : str - film rated, min len=2 max len=20,

    Output: rated_id: str - rated_id
    If there is an error in user input, it returns an exception with a description of the error."""

    # Check correct input
    if not isinstance(rated, str):
        return f'TypeError: rated type must be <class "str", not {type(rated)}>'

    if not 1 <= len(rated) >= 20:
        return 'ValueError: rated length must be between 1 and 20 characters, ' \
               f'you nickname length={len(rated)}'

    try:
        if get_rated(rated=rated) is not None:
            return 'This rated already exists'

        new_rated = Rateds(rated=rated)
        db.session.add(new_rated)
        db.session.commit()

        # get user_id of new user
        res_rated = get_rated(rated=rated)
        return res_rated

    except Exception as error:
        print(error)

    finally:
        return 'ServerError: Something went wrong'


def get_film_id(film_name: str):
    """Get film by id"""
    status = Films.query.filter_by(film_name=film_name).first()

    if status is None:
        return status
    return status.film_id


def get_film(film_name: str = None, film_id: int = None) -> list:
    """
    Input: str          - name of film_name from table films.film_name
        or
    Input: int          - film_id of rated from table films.film_id


    Output: film_name: str   - rated_id in table rateds.rated_id
        or
    Output: rated: str - rated in table rateds.rated
    """
    if film_name is not None:
        if not isinstance(film_name, str):
            return f'TypeError: Type film_name must bi <class "str"> not {type(film_name)}'

    # films = Films.query.filter(literal('e').contains(Films.film_name)).first()

    # films = Films.query.filter(Films.film_name.ilike(f'%{film_name}%')).all()
    # films = Films.query.with_entities(
    #         Films.film_name, Films.release_date
    #         ).filter(Films.film_name.ilike(f'%{film_name}%')).all()
    films = Films.query.filter(Films.film_name.ilike(f'%{film_name}%')).paginate()
    return films


def add_new_film(imdb_id: str, film_name: str, rated: str, poster_url: str,
                 release_date: str, rating: float, user_added: str,
                 genre: list[str], director: list[str], description: str = None) -> str:
    """Inputs:
    imdb_id: str        - id of film from imdb
    film_name: str      - name of films, length must be between 1 and unlimited.
    rated: str          - rated of film,like PG-13, R and etc.,
                          length must be between 1 and 20.
    poster_url: str     - url of film poster, length must be between 1 and unlimited
    release_date: str   - in ISO format like 1970-01-01, length = 10 characters.
    rating: float,      - film rating, must be between 0 and 10,  like 9.3
    user_added: str     - nickname of user, which add the film
    genre: list[str]    - list of film genres, like ['action', 'drama', etc.]
                           or ['action']
    director: list[str] - list of film directors,
                          like ['Christopher Nolan', 'Wes Anderson', etc.].
    description: str    - (optional field) film description, shot simple text
                          about the film default value = None.


    Output: film_id: str - film_id from table films.film_id

    If there is an error in user input, it returns an exception
    with a description of the error."""

    # Check correct input
    if not isinstance(imdb_id, str):
        return f'TypeError: imdb_id type must be <class "str", not {type(imdb_id)}>'
    if not isinstance(film_name, str):
        return f'TypeError: film_name type must be <class "str", not {type(film_name)}>'
    if not isinstance(rated, str):
        return f'TypeError: rated type must be <class "str", not {type(rated)}>'
    if not isinstance(poster_url, str):
        return 'TypeError: poster_url type must be <class "str", ' \
               f'not {type(poster_url)}>'
    if not isinstance(release_date, str):
        return 'TypeError: release_date type must be <class "str",' \
               f' not {type(release_date)}>'
    if not isinstance(rating, float):
        return 'TypeError: rating type must be <class "float", ' \
               f'not {type(rating)}>'
    if not isinstance(description, str):
        return 'TypeError: description type must be <class "str", ' \
               f'not {type(description)}>'
    if not isinstance(user_added, str):
        return 'TypeError: user_added type must be <class "str", ' \
               f'not {type(user_added)}>'
    if not isinstance(genre, list):
        return 'TypeError: genre type must be <class "list", ' \
               f'not {type(genre)}>'
    if not isinstance(director, list):
        return 'TypeError: director type must be <class "list", ' \
               f'not {type(director)}>'

    try:
        if get_film_id(film_name=film_name) is not None:
            return 'This film already exists'

        # get rated_id by rated name
        rated_name = int(get_rated(rated=rated))
        user_added = int(get_user_id(nickname=user_added))

        new_film = Films(film_name=film_name, rated=rated_name, poster_url=poster_url,
                         release_date=release_date, rating=rating, user_added=user_added,
                         description=description, imdb_id=imdb_id)

        db.session.add(new_film)
        db.session.commit()

        """Add links to the associative table.
        Because the variable director is a list with names, we loop through all the names
        and add everything one by one"""
        for dir_name in director:

            # checking if there is such a director in the database
            if get_director(name=dir_name) is None:
                add_new_director(name=dir_name)

            add_dir = Directors.query.filter_by(name=dir_name).first()

            # add director_id to associated table
            new_film.dir_films.append(add_dir)
        db.session.commit()
        """Add links to the associative table.
        Because the variable genres is a list with names, we loop through all the names
        and add everything one by one"""
        for gen_name in genre:

            # checking if there is such a director in the database

            print(get_genre(genre=gen_name))

            if get_genre(genre=gen_name) is None:

                add_new_genre(genre=gen_name)

            add_gen = Genres.query.filter_by(genre_name=gen_name).first()
            # add director_id to associated table
            new_film.gen_films.append(add_gen)

        db.session.commit()

        # get user_id of new user
        res_rated = get_film_id(film_name=film_name)
        return res_rated

    except Exception as error:
        print(error)
