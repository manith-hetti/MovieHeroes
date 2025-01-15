from lib.movie import Movie
from pymongo import DESCENDING, mongo_client
from flask import jsonify
from lib.database_connection import get_db

class MovieRepository:
    def __init__(self, db):
        self.db = db

    def find_movie_by_id(self, id, movie_table = "tmdbMovies") :
        movies = self.db[movie_table]
        print(id)
        found_movie = movies.find_one({"id": id})
        return Movie(
            found_movie["id"],
            found_movie["title"],
            found_movie["overview"],
            found_movie["poster_path"],
            found_movie["backdrop_path"],
            found_movie["vote_average"],
            found_movie["release_date"]
            )

    def find_top_movies(self, num_of_movies, movie_table = "tmdbMovies"):
        movies = self.db[movie_table]
        sorted_db_vote_average = movies.find({"vote_count": {"$gt": 1000}}).sort("vote_average", DESCENDING).limit(num_of_movies) #limit can be catered to our needs
        movies_as_dicts = list(sorted_db_vote_average)
        for movie in movies_as_dicts:
            movie['_id'] = str(movie['_id'])
            movie['vote_average'] = round(movie['vote_average']/2, 2)
        return movies_as_dicts

    def find_all(self):
        connection = self.db["tmdbMovies"]
        rows = connection.find()
        movies = []
        for row in rows:
            poster_path = row.get("poster_path", "")
            backdrop_path = row.get("backdrop_path", "")
            overview = row.get("overview", "")
            movie = Movie(row["id"], row["title"], overview, poster_path, backdrop_path, row["vote_average"], row["release_date"])
            movies.append(movie)
        return movies


    def find_all_movies(self, value):
        connection = self.db["tmdbMovies"]
        movies = connection.find({"title": {"$regex": value, "$options": "i"}})
        return list(movies)

    # This function is called when a user first signs up?
    def initial_rating_films(self):
        connection = self.db['tmdbMovies']
        movie_ids = [155, 157336, 694, 597, 68718, 497, 857, 585, 120, 1891]
        movies = []
        for id in movie_ids:
            movie = connection.find_one({'id': id})
            movie_dict = {'id': movie['id'], 'title': movie['title'], 'poster_path': movie['poster_path'], 'backdrop_path': movie['backdrop_path']}
            movies.append(movie_dict)
        return movies
