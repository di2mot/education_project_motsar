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
from filmBook.models import films_genres
from filmBook.models import films_directors
from filmBook import db
from datetime import date


def get_user_id(nickname: str) -> int:
    """
    Input: str - nickname of user from table users.nickname
    Output: int - user id in table users.id
    """

    if not isinstance(nickname, str):
        raise TypeError(f'Type nickname must bi <class "str"> not {type(nickname)}')

    user_id = Users.query.filter_by(nickname=nickname).first()

    if user_id is None:
        return user_id
    return user_id.id


def get_user_nickname(user_id: int) -> str:
    """
    Input: int - id of user from table users.id
    Output: str - user from table users.nickname
    """

    if not isinstance(user_id, int):
        return f'TypeError: Type id must be <class "int"> not {type(user_id)}'

    user_nick = Users.query.get(user_id)

    return user_nick


def get_user_auth(nickname: str, password: str) -> dict:
    """
    For authorization in flask-login
    Input: int - id of user from table users.id
    Output: str - nickname of user from table users.nickname
    """
    error = None
    status = False

    if not isinstance(nickname, str):
        error = f'TypeError: Type "nickname" must be <class "str"> not {type(nickname)}'
    if not isinstance(password, str):
        error = f'TypeError: Type "password" must be <class "str"> not {type(password)}'

    user = Users.query.filter_by(nickname='admin').first()
    if user is not None:
        if password == user.password:
            status = True
    else:
        error = f'LoginError: User {nickname} not find. For registration: /registration1 '

    return {'user': user, 'message': {'error': error, 'status': status}}


def get_user_password(user_id: str) -> str:
    """
    Input: int - id of user from table users.id
    Output: str - nickname of user from table users.nickname
    """

    if not isinstance(user_id, int):
        return f'TypeError:Type id must bi <class "int"> not {type(user_id)}'

    user_pass = Users.get(user_id)

    return user_pass.password


def add_new_user(nickname: str, email: str, password: str) -> str:
    """Create new user
    Input nickname : str - user nickname, min len=3 max len=20,
    Input email : str - user email, min len=5 max len=20,
    Input password : str - user password, min len=8 max len=120

    Output: str - id of new user
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
        # get id of new user
        user_id = get_user_id(nickname=nickname)

        return user_id

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

        return genre_id.genre_id

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
        # get id of new user
        genre_id = get_genre(genre=genre)

        return genre_id

    except Exception as error:
        print(error)


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

    if not 2 <= len(name) <= 40:
        return 'ValueError: nickname length must be between 2 and 40 characters, ' \
               f'you nickname length={len(name)}'

    try:
        if get_director(name) is not None:
            return 'This genre already exists'

        new_gir = Directors(name=name)
        db.session.add(new_gir)
        db.session.commit()

        # get id of new user
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

        # get id of new user
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
            return f'TypeError: Type film_name must be <class "str"> not {type(film_name)}'

    # films = Films.query.filter(literal('e').contains(Films.film_name)).first()

    films = Films.query.filter(Films.film_name.ilike(f'%{film_name}%')).all()
    # films = Films.query.with_entities(
    #         Films.film_name, Films.release_date
    #         ).filter(Films.film_name.ilike(f'%{film_name}%')).all()
    # films = Films.query.filter(Films.film_name.ilike(f'%{film_name}%')).paginate()
    return films


def get_full_film_info(film_name: str = '',
                       page: int = 1,
                       genre_list: list = None,
                       dir_list: list = None,
                       rel_start: int = 1900,
                       rel_fin: int = 2100,
                       order: str = None):

    """Get full film info use filters"""

    if order is not None:
        if order.lower() == 'rating':
            orderby = Films.rating
        elif order.lower() == 'release_date':
            orderby = Films.release_date
    else:
        orderby = None

    """How to create a bicycle using crutches"""

    names = ['film', 'film_id', 'film_name', 'rated', 'poster_url', 'release_date',
             'rating', 'nickname', 'imdb_id', 'description', 'genres', 'directors']
    # 1980-01-01
    # make date in datetime format
    start = date(rel_start, 1, 1)
    fin = date(rel_fin, 12, 31)

    # check genre
    if genre_list[0] is None:
        genre_list = []
        gen = Genres.query.add_columns(Genres.genre_name).all()
        for element in gen:
            genre_list.append(element[1])

    # check directors
    if dir_list[0] is None:
        dir_list = []
        dir = Directors.query.add_columns(Directors.name).all()
        for element in dir:
            dir_list.append(element[1])

    # SUPER-MEGA-GIPER-UlTRA query
    all_films = Films.query.select_from(Films)\
        .join(films_genres)\
        .join(films_directors)\
        .join(Genres)\
        .join(Directors)\
        .join(Rateds, Films.rateds_rated_id == Rateds.rated_id)\
        .join(Users, Films.user_added == Users.id)\
        .filter(
            (Films.film_name.ilike(f'%{film_name}%')) &
            (Films.film_id == films_genres.c.films_film_id) &
            (films_genres.c.genres_genre_id == Genres.genre_id) &
            (Genres.genre_name.in_(genre_list)) &
            (films_directors.c.directors_director_id == Directors.director_id) &
            (Directors.name.in_(dir_list)) &
            (Films.release_date.between(start, fin))) \
        .add_columns(
            Films.film_id,
            Films.film_name,
            Rateds.rated,
            Films.poster_url,
            Films.release_date,
            Films.rating,
            Users.nickname,
            Films.imdb_id,
            Films.description,
        ).order_by(orderby).paginate(page=page)

    all_genre = Films.query.select_from(Films).join(films_genres).join(Genres).filter(
      (Films.film_id == films_genres.c.films_film_id) &
      (films_genres.c.genres_genre_id == Genres.genre_id)
      ).add_columns(Films.film_id, Genres.genre_name).all()

    all_direcotrs = Films.query.select_from(Films).join(films_directors).join(Directors).filter(
      (Films.film_id == films_directors.c.films_film_id) &
      (films_directors.c.directors_director_id == Directors.director_id)
      ).add_columns(Films.film_id, Directors.name).all()

    # templ dicts
    gd = dict()
    dd = dict()

    # Add directors and genres to the dictionary gd and dd
    for i in all_genre:
        if i[0] not in gd:
            gd[i[0]] = []
        gd[i[0]].append(i[2])

    for i in all_direcotrs:
        if i[0] not in dd:
            dd[i[0]] = []
        if i[2] is not None:
            dd[i[0]].append(i[2])
        else:
            dd[i[0]].append('unknown')

    all_films = all_films.items

    for i, x in enumerate(all_films):
        x = list(x)
        all_films[i] = x
        all_films[i].append(','.join(gd[x[0]]))
        all_films[i].append(','.join(dd[x[0]]))
        a = all_films[i]
        all_films[i] = a

    new_list = []
    for element in all_films:
        new_list.append(dict(zip(names, element)))

    return new_list


def add_new_film(imdb_id: str, film_name: str, rated: str, poster_url: str,
                 release_date: str, rating: float, user_added: int,
                 genre: list[str], director: list[str], description: str = 'None',) -> str:
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
    if not isinstance(user_added, int):
        return 'TypeError: user_added type must be <class "int", ' \
               f'not {type(user_added)}>'
    if not isinstance(genre, list):
        return 'TypeError: genre type must be <class "list", ' \
               f'not {type(genre)}>'
    if not isinstance(director, list):
        return 'TypeError: director type must be <class "list", ' \
               f'not {type(director)}>'

    try:
        if get_film_id(film_name=film_name.lstrip().rstrip()) is not None:
            return 'This film already exists'

        # get rated_id by rated name
        rated_name = int(get_rated(rated=rated))
        # user_added = int(get_user_id(nickname=user_added))

        new_film = Films(film_name=film_name, rated=rated_name,
                         poster_url=poster_url,
                         release_date=release_date,
                         rating=rating, user_added=user_added,
                         description=description.lstrip().rstrip(), imdb_id=imdb_id)

        db.session.add(new_film)
        db.session.commit()

        """Add links to the associative table.
        Because the variable director is a list with names, we loop through all the names
        and add everything one by one"""
        for dir_name in director:
            # print(528, dir_name)
            # checking if there is such a director in the database
            # print(530, dir_name, get_director(name=dir_name.lstrip().rstrip()))
            if get_director(name=dir_name.lstrip().rstrip()) is None:
                add_new_director(name=dir_name.lstrip().rstrip())

            add_dir = Directors.query.filter_by(name=dir_name.lstrip().rstrip()).first()
            # print(535, add_dir, new_film.dir_films)
            # add director_id to associated table
            new_film.dir_films.append(add_dir)
        db.session.commit()

        """Add links to the associative table.
        Because the variable genres is a list with names, we loop through all the names
        and add everything one by one"""

        for gen_name in genre:

            # checking if there is such a director in the database
            # print(545, gen_name, get_genre(genre=gen_name.lstrip().rstrip()))
            if get_genre(genre=gen_name.lstrip().rstrip()) is None:
                add_new_genre(genre=gen_name.lstrip().rstrip())

            add_gen = Genres.query.filter_by(genre_name=gen_name.lstrip().rstrip()).first()
            # print(553, add_gen, new_film.gen_films)
            # add director_id to associated table
            new_film.gen_films.append(add_gen)

        db.session.commit()

        # get id of new user
        res_rated = get_film_id(film_name=film_name)

        return res_rated

    except Exception as error:
        print(error)


def update_film(film_id: int = None, imdb_id: str = None,
                film_name: str = None, rated: str = None,
                poster_url: str = None, release_date: str = None,
                rating: float = None, user_added: str = None,
                genre: list[str] = None, director: list[str] = None,
                description: str = 'None') -> bool:

    """Update information about the film"""

    status = False

    # Film object for update
    film = Films.query.get(film_id)

    if film.user_added in (1, user_added):

        if imdb_id:
            film.imdb_id = imdb_id
        if film_name:
            film.film_name = film_name
        if rated:
            film.rated = int(get_rated(rated=rated))
        if poster_url:
            film.poster_url = poster_url
        if release_date:
            film.release_date = release_date
        if rating:
            film.rating = float(rating)
        if user_added:
            film.user_added = int(get_user_id(nickname=user_added))
        if genre:
            for gen in genre:
                new_gen = int(get_genre(genre=gen))
                gen_class = films_genres.query.filter_by(films_film_id=film_id)
                gen_class.genres_genre_id = new_gen
        if director:
            for dirct in director:
                new_dir = int(get_director(name=dirct))
                dir_class = films_directors.query.filter_by(films_film_id=film_id)
                dir_class.directors_director_id = new_dir
        if description:
            film.description = description
        db.session.add(film)
        db.session.commit()
        status = True

    return status


def delete_film(film_id: int, user_id: int) -> dict:
    """
    Delete film
    input: film_id: str - name of director
    output: dict[boolen] """
    status = False
    films = db.session.query(Films).filter(Films.film_id == film_id).first()
    if films.user_added in (1, user_id):
        db.session.delete(films)
        db.session.commit()
        status = True
    return {'status': status}


def delete_directors(director_name: str, user_id: int) -> dict:
    """
    Delete director
    input: director_name: str - name of director
    output: dict[boolen]
    """
    status = False
    if user_id == 1:

        direct = Directors.query.filter_by(name=director_name).first()
        db.session.delete(direct)
        db.session.commit()
        status = True

    return {'status': status}
