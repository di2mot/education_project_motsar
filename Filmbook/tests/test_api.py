#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""tests"""
# =============================================================================
# Imports
# =============================================================================
import pytest
from tests.resources import test_film, test_film_update
from filmBook import app, db_core


@pytest.fixture
def client():
    """Create test_client for testing app"""

    test_app = app.test_client({
                                'TESTING': True
                                })
    with test_app as client:
        yield client


# =============================================================================
"""TESTING USERS"""
# =============================================================================

class AuthActions(object):
    """Class for authorization"""

    def __init__(self, client):
        self._client = client

    def login(self, nickname='admin', password='admin'):
        """Test user login"""
        return self._client.post(
                                    '/login',
                                    data={
                                            'nickname': nickname,
                                            'password': password
                                        }
                                )

    def logout(self):
        """Test user logout"""
        return self._client.post('/logout')

    def registration(self, nickname, email, password):
        """Test user registration"""
        return self._client.post(
                                    '/registration',
                                    data={
                                        'nickname': nickname,
                                        'email': email,
                                        'password': password
                                        }
                                )


@pytest.fixture
def auth(client):
    """Preparation for test user login """

    return AuthActions(client)


def test_auth_login(client, auth):
    """Testing login"""

    response = auth.login()
    assert response.status_code == 200
    assert response.json['login']['error'] is None
    assert response.json['login']['status'] is True


def test_auth_logout(client, auth):
    """Testing logout"""
    # for first login on the server
    auth.login()
    # logout from the server
    response = auth.logout()
    assert response.status_code == 200
    assert response.json['logout']['status'] is True


def test_user_registration(client, auth):
    """Test registration"""

    nickname = 'test_user'
    email = 'test@mail.com'
    password = 'test_user'
    user_id = 0

    new_uer = auth.registration(
                                nickname=nickname,
                                email=email,
                                password=password
                                )

    user_id = new_uer.json['new_user']['status']

    assert isinstance(user_id, int)
    assert new_uer.status_code == 200

    # test new_user
    response = auth.login(nickname=nickname, password=password)

    assert response.status_code == 200
    assert response.json['login']['error'] is None
    assert response.json['login']['status'] is True
    # for first login on the server

    # logout from the server
    response = auth.logout()
    assert response.status_code == 200
    assert response.json['logout']['status'] is True

    # delete test user
    db_core.delete_user(nickname=nickname)


# =============================================================================
"""TESTING FILMS"""
# =============================================================================



class FilmEngine(object):
    """Class for testig films"""

    def __init__(self, client):
        self._client = client

    def add_films(self, data: dict):
        """Test add film"""

        return self._client.post('/add_film', data=data)

    def update_film(self, film_id: int, data: dict):
        """Test update film"""
        data['film_id'] = film_id
        return self._client.put('/add_film', data=data)

    def search_films(self, film_name):
        """Test search_films"""
        return self._client.get(f'/films?&name={film_name}')

    def delete_film(self, film_id):
        """Test search_films"""
        return self._client.delete(f'/films?&film_id={film_id}')


@pytest.fixture
def film(client):
    """Preparation for test user login """

    return FilmEngine(client)


def test_film_param(client, film, auth):
    """Testing GET film, ADD film, UPDATE film, DELETE flm"""

    auth.login()

    # add film
    response_add = film.add_films(test_film)
    film_id = response_add.json['new_films']['film_id']

    assert response_add.status_code == 200
    assert isinstance(film_id, int)
    assert film_id is not None

    # search films
    response_search = film.search_films(test_film["film_name"])
    assert response_search.status_code == 200
    assert response_search.json['films'][0]['film_id'] == film_id

    # update film
    response_update = film.update_film(film_id, test_film_update)
    assert response_update.status_code == 200
    assert response_update.json['update_films']['status'] is True

    # delete test film
    response_delete = film.delete_film(film_id)
    assert response_delete.status_code == 200
    assert response_delete.json['films']['status'] is True

    # Logout test user
    auth.logout()







