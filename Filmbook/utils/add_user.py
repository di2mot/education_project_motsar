from filmBook.db_core import *
import csv
import hashlib
import random


def add_users():
    """Add users to the table Users"""

    add_admin = add_new_user(nickname='admin', email='admin@mail.com',
                                password='admin')
    for i in range(2, 100):
        new_user = add_new_user(nickname=f'user{i}', email=f'user{i}@gmail.com',
                                password=f'{hashlib.sha1(str(i).encode()).hexdigest()}')


def add_films_to_table():
    """Add films, genres, directors"""

    with open("films.csv", encoding='utf-8') as r_file:

        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            imdb_id: str = row[1].lstrip().rstrip()
            film_name: str = row[2].lstrip().rstrip()
            rated: str = row[3].lstrip().rstrip()
            poster_url: str = row[4].lstrip().rstrip()
            release_date: str = row[5].lstrip().rstrip()
            rating: float = float(row[6])
            description: str = row[7].lstrip().rstrip()
            user_added: int = random.randint(1, 99)
            genre: list[str] = row[9].split(',')
            director: list[str] = row[10].split(',')

            new_film = add_new_film(imdb_id=imdb_id,
                                    film_name=film_name,
                                    rated=rated,
                                    poster_url=poster_url,
                                    release_date=release_date,
                                    rating=rating,
                                    description=description,
                                    user_added=user_added,
                                    genre=genre,
                                    director=director)




if __name__ == "__main__":
    add_users()
    add_films_to_table()

