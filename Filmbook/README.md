FilmBook Flask-RESTFull API application 

by

Motsar Dima

For run app into the Docker run:

`docker-compose --env-file ./.env.list up -d`

next, run:


`docker-compose --env-file ./.env.list exec db psql -U postgres -c "CREATE DATABASE filmbook;` 

To make mirgation run:


`flask db init`

`flask db migrate`

`flask db upgrage`

To create a test database, run:

`./utils/add_user.py`

This will automatically create a database along with users, movies, genres and directors.
Once added, you can take full advantage of the API without having to manually add it.
